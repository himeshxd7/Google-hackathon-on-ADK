import google.generativeai as genai
import os

class SummarizerAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = genai.GenerativeModel("gemini-2.0-flash").start_chat(history=[])

    def run(self, input: dict):
        url = input.get("url")
        lang = input.get("lang", "en")
        prompt = f"You are a blog assistant. Respond in {lang.upper()}.\nSummarize this article in 3–4 short, simple lines:\n{url}"
        try:
            return self.chat.send_message(prompt).text.strip()
        except Exception as e:
            return f"Summary unavailable: {str(e)}"
