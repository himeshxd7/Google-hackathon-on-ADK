from flask import Flask, render_template, request, send_file
import os
import markdown2

from agents.news_reader import NewsReaderAgent
from agents.summarizer import SummarizerAgent
from agents.explainer import ExplainerAgent
from agents.context_research import ContextResearchAgent
from agents.image_finder import ImageFinderAgent
from agents.coordinator import CoordinatorAgent

app = Flask(__name__)

reader = NewsReaderAgent()
summarizer = SummarizerAgent()
explainer = ExplainerAgent()
researcher = ContextResearchAgent()
image_finder = ImageFinderAgent()
coordinator = CoordinatorAgent(reader, summarizer, explainer, image_finder, researcher)

@app.route('/')
def home():
    return render_template("blog.html", posts=[], categories=[
        "general", "world", "nation", "business", "technology", "sports", "science"
    ])

@app.route('/generate')
def generate_blog():
    category = request.args.get("category", "general")
    query = request.args.get("query", "")
    lang = request.args.get("lang", "en")

    blog_posts = coordinator.handle_blog_generation(category, query, lang)

    # Save for download
    full_md = ""
    for post in blog_posts:
        full_md += f"# {post['title']}\n\n![Image]({post['image_url']})\n\n" \
                   f"## 🔹 Summary:\n{post['summary']}\n\n" \
                   f"## 🔹 Background:\n{post['background']}\n\n" \
                   f"## 🔹 Key Terms:\n{post['terms']}\n\n---\n\n"

    with open("static/latest_blog.md", "w", encoding="utf-8") as f:
        f.write(full_md)

    with open("static/latest_blog.html", "w", encoding="utf-8") as f:
        f.write("".join([
            f"<h2>{p['title']}</h2><img src='{p['image_url']}'><br><b>Summary:</b><p>{p['summary']}</p><b>Background:</b><p>{p['background']}</p><b>Key Terms:</b><p>{p['terms']}</p><hr>"
            for p in blog_posts
        ]))

    return render_template("blog.html", posts=blog_posts, categories=[
        "general", "world", "nation", "business", "technology", "sports", "science"
    ])

@app.route('/download/<fmt>')
def download(fmt):
    path = f"static/latest_blog.{fmt}"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)
