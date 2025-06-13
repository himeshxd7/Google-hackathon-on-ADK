import google.generativeai as genai
import os

class ExplainerAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.chat = genai.GenerativeModel("gemini-2.0-flash").start_chat(history=[])

    def run(self, input: dict):
        text = input.get("text")
        lang = input.get("lang", "en")
        prompt = f"Explain any complex or technical terms from this summary. Respond in {lang.upper()}:\n{text}"
        try:
            return self.chat.send_message(prompt).text.strip()
        except Exception as e:
            return f"Explanation unavailable: {str(e)}"
