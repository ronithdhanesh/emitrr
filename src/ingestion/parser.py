from typing import List, Dict
import re


class TranscriptParser:
    """
    Parses raw physician-patient transcripts into structured dialogue turns.
    """

    SPEAKER_PATTERN = re.compile(r"^(Physician|Doctor|Patient):\s*(.*)", re.I)

    def parse(self, text: str) -> List[Dict[str, str]]:
        dialogue = []

        for line in text.split("\n"):
            line = line.strip()
            if not line:
                continue

            match = self.SPEAKER_PATTERN.match(line)
            if match:
                speaker, content = match.groups()
                dialogue.append({
                    "speaker": speaker.lower(),
                    "text": content.strip()
                })

        return dialogue
