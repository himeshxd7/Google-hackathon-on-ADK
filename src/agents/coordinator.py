class CoordinatorAgent:
    def __init__(self, reader, summarizer, explainer, image_finder, researcher):
        self.reader = reader
        self.summarizer = summarizer
        self.explainer = explainer
        self.image_finder = image_finder
        self.researcher = researcher

    def handle_blog_generation(self, category, query, lang):
        articles = self.reader.run({"query": query, "category": category, "lang": lang})
        blog_posts = []
        for a in articles:
            url = a["url"]
            title = a["title"]
            summary = self.summarizer.run({"url": url, "lang": lang})
            background = self.researcher.run({"topic": title, "lang": lang})
            terms = self.explainer.run({"text": summary, "lang": lang})
            image = self.image_finder.run({"query": title})
            blog_posts.append({
                "title": title,
                "summary": summary,
                "background": background,
                "terms": terms,
                "image_url": image
            })
        return blog_posts
