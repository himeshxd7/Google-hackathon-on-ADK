import requests
import os

class ImageFinderAgent:
    def run(self, input: dict):
        query = input.get("query")
        headers = {"Authorization": f"Client-ID {os.getenv('UNSPLASH_API_KEY')}"}
        try:
            res = requests.get(f"https://api.unsplash.com/search/photos?query={query}&per_page=1", headers=headers)
            return res.json()["results"][0]["urls"]["regular"]
        except:
            return "https://via.placeholder.com/300"
