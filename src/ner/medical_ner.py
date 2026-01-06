import spacy
from typing import Dict, List


class MedicalNER:
    def __init__(self):
        self.nlp = spacy.load("en_core_sci_sm")

        self.CATEGORY_MAP = {
            "SYMPTOM": "Symptoms",
            "DISEASE": "Diagnosis",
            "TREATMENT": "Treatment",
            "PROCEDURE": "Treatment"
        }

    def extract(self, texts: List[str]) -> Dict[str, List[str]]:
        results = {
            "Symptoms": [],
            "Diagnosis": [],
            "Treatment": [],
            "Prognosis": []
        }

        for text in texts:
            doc = self.nlp(text)

            for ent in doc.ents:
                label = ent.label_.upper()
                if label in self.CATEGORY_MAP:
                    category = self.CATEGORY_MAP[label]
                    results[category].append(ent.text)

            if "recover" in text.lower() or "full recovery" in text.lower():
                results["Prognosis"].append("Full recovery expected")

        for key in results:
            results[key] = list(set(results[key]))

        return results
