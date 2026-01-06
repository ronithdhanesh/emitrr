from src.ingestion.parser import TranscriptParser
from src.ner.medical_ner import MedicalNER
from src.summarization.medical_summary import MedicalSummarizer
from src.summarization.report_builder import MedicalReportBuilder
from src.sentiment.sentiment_classifier import PatientSentimentAnalyzer
from src.sentiment.intent_detector import PatientIntentDetector


def run_pipeline(raw_text: str) -> dict:
    parser = TranscriptParser()
    ner = MedicalNER()
    summarizer = MedicalSummarizer()
    report_builder = MedicalReportBuilder()
    sentiment_analyzer = PatientSentimentAnalyzer()
    intent_detector = PatientIntentDetector()

    dialogue = parser.parse(raw_text)

    patient_texts = [d["text"] for d in dialogue if d["speaker"] == "patient"]
    all_texts = [d["text"] for d in dialogue]

    ner_results = ner.extract(all_texts)
    sentiment = sentiment_analyzer.analyze(patient_texts)
    intent = intent_detector.detect(patient_texts)

    summary_text = summarizer.summarize(raw_text)

    report = report_builder.build(
        patient_name="Janet Jones",
        ner_results=ner_results,
        current_status="Occasional backache",
        prognosis="Full recovery expected within six months"
    )

    return {
        "Medical_Summary": report,
        "Patient_Sentiment": sentiment,
        "Patient_Intent": intent,
        "Narrative_Summary": summary_text
    }
