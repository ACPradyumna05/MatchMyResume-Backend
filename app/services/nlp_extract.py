import spacy

class NLPExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_skills(self, text: str):
        doc = self.nlp(text)
        skills = set()
        for chunk in doc.noun_chunks:
            if len(chunk.text) < 40:
                skills.add(chunk.text.lower())
        for token in doc:
            if token.pos_ in {"NOUN", "PROPN"}:
                skills.add(token.text.lower())
        return list(skills)
