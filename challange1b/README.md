```text
challange1b/
├── app/
│   ├── main.py                  # Entry point that iterates over all collections
│   ├── process.py               # Loads persona & job, calls extraction logic
│   ├── utils.py                 # Core logic: PDF reading, ONNX model, scoring
│   ├── model.onnx               # Lightweight semantic model (~90MB, MiniLM)
│   └── requirements.txt         # All Python dependencies

├── Challenge_1b/                # Main challenge folder with multiple test collections
│   ├── Collection 1/
│   │   ├── challenge1b_input.json
│   │   ├── challenge1b_output.json
│   │   └── PDFs/
│   │       ├── South of France - Cities.pdf
│   │       ├── South of France - Cuisine.pdf
│   │       └── ...
│   ├── Collection 2/
│   │   ├── challenge1b_input.json
│   │   ├── challenge1b_output.json
│   │   └── PDFs/
│   │       └── ...
│   └── Collection 3/
│       ├── challenge1b_input.json
│       ├── challenge1b_output.json
│       └── PDFs/
│           └── ...

├── Dockerfile                  # Builds the offline inference container
├── README.md                   # Clean, professional project guide
├── approach_explanation.md     # Written methodology for Adobe judging panel
```

...............................................................................................................................................................................
#  Adobe Hackathon 2025 – Challenge 1B  
###  Persona-Driven PDF Section Extractor  
**Team Name**: UV Boys 
**Challenge ID**: Round 1B  
**Submission Date**: July 27, 2025  

---

##  Overview

This solution addresses the Adobe Hackathon 2025 Challenge 1B:  
> “Connect What Matters — For the User Who Matters.”

Our system intelligently analyzes a collection of PDF documents and extracts the **most relevant sections and sub-sections** tailored to a **specific persona** and their **job-to-be-done**. The output is a structured, ranked JSON file that helps surface the most meaningful content in a human-like, AI-assisted manner — all while respecting Adobe's strict **performance**, **model size**, and **offline execution** constraints.

---

##  Key Features

-  **Offline & Lightweight** (≤1GB Docker image)
-  **Fully CPU-based** – No GPU or external dependencies
-  **Semantic Section Ranking** using ONNX-based Transformer
-  **Personalized Output** based on persona + task
-  **Structured JSON** in Adobe’s required format
-  **Fast Execution** – <60 seconds for 3–5 PDFs
-  Future-ready architecture: modular, extensible, and production-friendly

 ## For more explanation of used logic : [Explanation](challange1b/Approach%20Explanation.md)

  
# Challenge 1B - Persona PDF Analyzer

## How to Use

1.  Place your PDFs and `challenge1b_input.json` inside each `Collection` folder  
2.  Build Docker image:
   ```bash
   docker build -t challenge1b-lite .
   ```
3.  Run analysis:
   ```bash
   docker run --rm -v "${PWD}/Challenge_1b:/app/Challenge_1b" challenge1b-lite
   ```

 If using Windows, use this in PowerShell:

```powershell
$vol = (Get-Location).Path + "\Challenge_1b"
docker run --rm -v "${vol}:/app/Challenge_1b" challenge1b-lite
```

---

##  HOW TO SET IT UP

### Step 1: Create this folder structure
Put all the provided files into correct subfolders. You can unzip or copy-paste.

### Step 2: Add your PDFs and `challenge1b_input.json` inside:
- `Challenge_1b/Collection 1/`
- `Challenge_1b/Collection 2/`
- `Challenge_1b/Collection 3/`

### Step 3: Then run:
```bash
docker build -t challenge1b-lite .
docker run --rm -v "${PWD}/Challenge_1b:/app/Challenge_1b" challenge1b-lite
```
