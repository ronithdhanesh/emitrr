```markdown
# 🩺 Physician Notetaker

An end-to-end **clinical NLP system** for medical transcription analysis, built to extract structured medical information, analyze patient sentiment and intent, and generate clinically readable notes from raw physician–patient conversations.

This project demonstrates **production-minded NLP engineering** using a hybrid of **rule-based logic and transformer models**, with full **Docker-based reproducibility**.

---

## 📌 Project Objectives

The system processes a raw medical conversation transcript and produces:

1. **Medical NLP Summarization**

   - Named Entity Recognition (NER)
   - Keyword extraction
   - Structured medical summary (JSON)

2. **Sentiment & Intent Analysis**

   - Patient emotional state
   - Patient intent (e.g., seeking reassurance)

3. **SOAP Note Generation (Bonus)**
   - Subjective
   - Objective
   - Assessment
   - Plan

---

## 🧠 System Design Philosophy

This project intentionally **does not rely on a single LLM prompt**.

Instead, it follows **real-world healthcare NLP principles**:

- Deterministic logic for factual medical data
- Transformer models where language understanding is needed
- Hybrid ML + rules for safety, interpretability, and robustness
- Clear separation of concerns (ingestion, NER, sentiment, orchestration)

This mirrors how **production medical NLP systems** are actually built.

---

## 🗂️ Project Structure
```

physician-notetaker/
│
├── data/
│ ├── raw/
│ │ └── sample_transcript.txt
│ └── processed/
│
├── src/
│ ├── ingestion/
│ │ └── parser.py
│ ├── ner/
│ │ └── medical_ner.py
│ ├── summarization/
│ │ ├── keywords.py
│ │ ├── medical_summary.py
│ │ └── report_builder.py
│ ├── sentiment/
│ │ ├── sentiment_classifier.py
│ │ └── intent_detector.py
│ ├── soap/
│ │ └── soap_generator.py
│ ├── utils/
│ │ └── helpers.py
│ └── pipeline.py
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md

````

---

## 🔍 Component Breakdown

### 1️⃣ Transcript Ingestion

**Purpose:**
Convert raw transcript text into structured dialogue turns.

**Key Features:**
- Speaker-aware parsing (Patient vs Physician)
- Normalization of speaker labels
- Noise-resistant parsing

**Output Example:**
```json
[
  { "speaker": "patient", "text": "I had neck and back pain" },
  { "speaker": "physician", "text": "Did you seek treatment?" }
]
````

---

### 2️⃣ Medical Named Entity Recognition (NER)

**Purpose:**
Extract clinically relevant entities.

**Model Used:**

- `en_core_sci_sm` (SciSpacy)

**Extracted Categories:**

- Symptoms
- Diagnosis
- Treatment
- Prognosis (rule-augmented)

**Why SciSpacy?**

- Trained on biomedical corpora
- Better medical vocabulary coverage than general NLP models
- Lightweight and explainable

---

### 3️⃣ Keyword Extraction

**Purpose:**
Capture clinically important phrases that may not be standard entities.

**Tool Used:**

- KeyBERT (`all-MiniLM-L6-v2`)

**Examples:**

- “whiplash injury”
- “physiotherapy sessions”
- “occasional back pain”

**Why This Matters:**
NER captures _what_, keywords capture _what matters_.

---

### 4️⃣ Medical Summarization

**Purpose:**
Condense the full transcript into a narrative summary.

**Model Used:**

- `facebook/bart-large-cnn`

**Important Design Choice:**

- The model summarizes **text only**
- It does **not** decide structured medical facts

This prevents hallucination and preserves clinical safety.

---

### 5️⃣ Structured Medical Report (JSON)

**Purpose:**
Produce a deterministic, schema-validated medical summary.

**Example Output:**

```json
{
  "Patient_Name": "Janet Jones",
  "Symptoms": ["Neck pain", "Back pain", "Head impact"],
  "Diagnosis": "Whiplash injury",
  "Treatment": ["10 physiotherapy sessions", "Painkillers"],
  "Current_Status": "Occasional backache",
  "Prognosis": "Full recovery expected within six months"
}
```

**Handling Missing or Ambiguous Data:**

- Defaults to `"Unknown"`
- Rule-based inference when safe
- No guessing or hallucination

---

### 6️⃣ Sentiment Analysis

**Purpose:**
Identify the patient’s emotional state.

**Model Used:**

- `distilbert-base-uncased-finetuned-sst-2-english`

**Domain Mapping:**

- Negative → `Anxious`
- Neutral → `Neutral`
- Positive → `Reassured`

**Only patient dialogue is analyzed.**

---

### 7️⃣ Intent Detection

**Purpose:**
Understand _why_ the patient is speaking.

**Approach:**

- Rule-based phrase detection
- Domain-specific triggers

**Detected Intents:**

- Reporting symptoms
- Seeking reassurance
- Neutral inquiry

This hybrid approach is more reliable than pure ML for clinical text.

---

### 8️⃣ SOAP Note Generation (Bonus)

**Purpose:**
Generate structured clinical documentation.

**SOAP Sections:**

- **Subjective:** Patient-reported symptoms
- **Objective:** Physician observations
- **Assessment:** Diagnosis and severity
- **Plan:** Treatment and follow-up

**Why Rule-Based First?**
SOAP notes require logical structure more than language creativity.

---

## 🔁 End-to-End Pipeline

The full pipeline is orchestrated via:

```bash
python src/pipeline.py
```

**Pipeline Output Includes:**

- Structured medical summary
- Patient sentiment
- Patient intent
- SOAP note
- Narrative summary

---

## 🐳 Docker Support (Reproducible Execution)

This project is fully Dockerized.

### Build Image

```bash
docker build -t physician-notetaker .
```

### Run Pipeline

```bash
docker run --rm physician-notetaker
```

### Run with Mounted Data

```bash
docker run --rm \
  -v $(pwd)/data:/app/data \
  physician-notetaker
```

**Why Docker?**

- Eliminates environment issues
- Handles heavy ML dependencies safely
- Reproducible across machines

---

## 📚 Model & Dataset References

### Models

- SciSpacy (`en_core_sci_sm`)
- BART (`facebook/bart-large-cnn`)
- DistilBERT (SST-2)

### Datasets for Fine-Tuning (Future Work)

- MIMIC-III
- i2b2 Clinical NLP
- n2c2
- MedDialog

---

## 🧪 Testing Strategy

- Unit tests for ingestion and parsing
- Deterministic outputs for structured fields
- Graceful handling of missing data
- Confidence-based sentiment thresholds

---

## 🚀 Future Improvements

- FastAPI inference service
- GPU-enabled Docker image
- Fine-tuned medical sentiment model
- Confidence scoring for extracted entities
- ONNX optimization for faster inference

---

## 🏁 Final Notes

This project prioritizes:

- Clinical safety
- Explainability
- Modular design
- Production readiness

It is intentionally **not over-engineered**, yet easily extensible — a balance expected in real-world healthcare NLP systems.

---

**Author:**
Built with a senior-engineer mindset for real-world clinical NLP applications.

```

```
