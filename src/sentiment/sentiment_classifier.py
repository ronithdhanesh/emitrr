from transformers import pipeline
from typing import List


class PatientSentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze(self, patient_texts: List[str]) -> str:
        if not patient_texts:
            return "Neutral"

        combined_text = " ".join(patient_texts)
        result = self.classifier(combined_text)[0]

        label = result["label"]
        score = result["score"]

        if label == "NEGATIVE" and score > 0.6:
            return "Anxious"
        if label == "POSITIVE" and score > 0.6:
            return "Reassured"

        return "Neutral"
