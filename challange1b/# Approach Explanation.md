#  Approach Explanation – Adobe Hackathon Round 1B

##  Objective

Our solution aims to intelligently extract and rank the most relevant sections and sub-sections from a collection of PDFs based on a **persona** and their **job-to-be-done**, fully aligned with Adobe's “Connecting the Dots” theme. The system operates entirely **offline**, with a model size under **1GB**, and processes input in **under 60 seconds**.

---

##  Workflow Overview

### 1. Input Parsing  
The system begins by reading a JSON configuration (`challenge1b_input.json`) which provides:
- A **persona** (e.g., "Travel Planner")
- A **job-to-be-done** (e.g., "Plan a trip of 4 days for 10 college friends")

These two inputs are semantically combined into a query string for relevance scoring.

---

### 2. Lightweight Semantic Embedding  
To ensure fast and offline compatibility, we use a **compressed ONNX-based MiniLM model (~90MB)** loaded via `onnxruntime`. It converts the input query and document content into embedding vectors for scoring.

> This approach ensures compatibility with Adobe's 1GB Docker image constraint and CPU-only environment.

---

### 3. PDF Parsing  
Each document is processed using `PyMuPDF`, extracting full page-wise text. This enables:
- Per-page content understanding
- Section boundary detection (optional heading logic can be plugged in)

---

### 4. Relevance Scoring & Ranking  
Each document (or section) is semantically compared to the query using **cosine similarity** of embeddings. This generates a **relevance score** for ranking.

- **Top-level sections** are added to `extracted_sections`
- **Refined content** (snippets or summaries) are included in `subsections`
- Sections are sorted by **importance_rank** in descending order

---

## 📤 Output Format

The final output JSON follows Adobe’s specification:
- `metadata`: documents, persona, job, timestamp
- `extracted_sections`: document, section title, page, rank
- `subsections`: document, refined text, page, rank

---

## Constraints Respected

| Constraint            | Compliant |
|-----------------------|-----------|
| Offline Execution     | ✅ Yes    |
| Docker Image < 1GB    | ✅ Yes (~500MB) |
| CPU-only Processing   | ✅ Yes    |
| Execution < 60 sec    | ✅ Yes    |
| Output Format         | ✅ Fully Aligned |

---

##  Technologies Used

- `PyMuPDF` for PDF parsing  
- `onnxruntime` for fast local inference  
- `transformers` for tokenization  
- `numpy` for vector math  
- `Docker` for containerization  

---

##  Why This Works

Instead of relying on surface-level matching (e.g., keywords or font size), our system understands documents **semantically**. The persona-objective combination drives a **smart similarity score**, helping identify **what truly matters** to the user.

The result: an **intelligent document assistant** that extracts relevant, ranked, and contextual content — not just raw text.

---

##  Future Improvements

- Heading-level detection based on font sizes + layout
- Fine-tuned multilingual model for Japanese or Hindi
- Richer sub-section clustering for larger documents

---

##  Thank You

We're excited to help reimagine the future of intelligent document experiences with Adobe.

