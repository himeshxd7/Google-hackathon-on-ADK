import requests
import os

class NewsReaderAgent:
    def run(self, input: dict):
        query = input.get("query", "")
        category = input.get("category", "general")
        lang = input.get("lang", "en")
        key = os.getenv("GNEWS_API_KEY")
        if query:
            url = f"https://gnews.io/api/v4/search?q={query}&lang={lang}&token={key}"
        else:
            url = f"https://gnews.io/api/v4/top-headlines?lang={lang}&topic={category}&token={key}"
        try:
            return requests.get(url).json().get("articles", [])[:2]
        except:
            return []
