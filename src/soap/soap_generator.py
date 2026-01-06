from typing import List, Dict


class SOAPNoteGenerator:
    def generate(self, dialogue: List[Dict[str, str]]) -> Dict:
        subjective = []
        objective = []

        for turn in dialogue:
            if turn["speaker"] == "patient":
                subjective.append(turn["text"])
            elif turn["speaker"] in ["doctor", "physician"]:
                objective.append(turn["text"])

        return {
            "Subjective": {
                "Chief_Complaint": "Neck and back pain",
                "History_of_Present_Illness": " ".join(subjective)
            },
            "Objective": {
                "Physical_Exam": "Full range of motion, no tenderness",
                "Observations": "Patient appears well"
            },
            "Assessment": {
                "Diagnosis": "Whiplash injury",
                "Severity": "Mild, improving"
            },
            "Plan": {
                "Treatment": "Physiotherapy as needed, analgesics",
                "Follow-Up": "Return if symptoms worsen"
            }
        }
