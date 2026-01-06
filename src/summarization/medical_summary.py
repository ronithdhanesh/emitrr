from transformers import pipeline
from typing import Dict, List


class MedicalSummarizer:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text: str) -> str:
        summary = self.summarizer(
            text,
            max_length=180,
            min_length=60,
            do_sample=False
        )

        return summary[0]["summary_text"]
