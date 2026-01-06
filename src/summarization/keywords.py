from keybert import KeyBERT
from typing import List


class MedicalKeywordExtractor:
    def __init__(self):
        self.model = KeyBERT(model="all-MiniLM-L6-v2")

    def extract(self, text: str, top_n: int = 10) -> List[str]:
        keywords = self.model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            stop_words="english",
            top_n=top_n
        )

        return [kw[0] for kw in keywords]
