from typing import Dict, List


class MedicalReportBuilder:
    def build(
        self,
        patient_name: str,
        ner_results: Dict[str, List[str]],
        current_status: str,
        prognosis: str
    ) -> Dict:
        return {
            "Patient_Name": patient_name,
            "Symptoms": ner_results.get("Symptoms", []),
            "Diagnosis": (
                ner_results.get("Diagnosis", [None])[0]
                if ner_results.get("Diagnosis") else "Unknown"
            ),
            "Treatment": ner_results.get("Treatment", []),
            "Current_Status": current_status or "Unknown",
            "Prognosis": prognosis or "Unknown"
        }
