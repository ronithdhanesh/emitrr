from typing import List


class PatientIntentDetector:
    def detect(self, patient_texts: List[str]) -> str:
        text = " ".join(patient_texts).lower()

        if any(phrase in text for phrase in [
            "worried", "concerned", "will this", "affect me", "long term"
        ]):
            return "Seeking reassurance"

        if any(phrase in text for phrase in [
            "pain", "hurt", "ache", "discomfort", "stiff"
        ]):
            return "Reporting symptoms"

        return "Neutral inquiry"
