import wikipedia

class ContextResearchAgent:
    def run(self, input: dict):
        topic = input.get("topic")
        lang = input.get("lang", "en")
        try:
            wikipedia.set_lang(lang)
            return wikipedia.summary(topic, sentences=2)
        except:
            return "Background information not available."
