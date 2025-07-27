# Challenge 1B - Persona PDF Analyzer

## How to Use

1. 🗂️ Place your PDFs and `challenge1b_input.json` inside each `Collection` folder  
2. 🛠️ Build Docker image:
   ```bash
   docker build -t challenge1b-lite .
   ```
3. 🚀 Run analysis:
   ```bash
   docker run --rm -v "${PWD}/Challenge_1b:/app/Challenge_1b" challenge1b-lite
   ```

💡 If using Windows, use this in PowerShell:

```powershell
$vol = (Get-Location).Path + "\Challenge_1b"
docker run --rm -v "${vol}:/app/Challenge_1b" challenge1b-lite
```

---

## 🛠️ HOW TO SET IT UP

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
...............................................................................................................................................................................
# 📘 Adobe Hackathon 2025 – Challenge 1B  
### 🚀 Persona-Driven PDF Section Extractor  
**Team Name**: UV Boys 
**Challenge ID**: Round 1B  
**Submission Date**: July 27, 2025  

---

## 🧠 Overview

This solution addresses the Adobe Hackathon 2025 Challenge 1B:  
> “Connect What Matters — For the User Who Matters.”

Our system intelligently analyzes a collection of PDF documents and extracts the **most relevant sections and sub-sections** tailored to a **specific persona** and their **job-to-be-done**. The output is a structured, ranked JSON file that helps surface the most meaningful content in a human-like, AI-assisted manner — all while respecting Adobe's strict **performance**, **model size**, and **offline execution** constraints.

---

## 🔧 Key Features

- ✅ **Offline & Lightweight** (≤1GB Docker image)
- ✅ **Fully CPU-based** – No GPU or external dependencies
- ✅ **Semantic Section Ranking** using ONNX-based Transformer
- ✅ **Personalized Output** based on persona + task
- ✅ **Structured JSON** in Adobe’s required format
- ✅ **Fast Execution** – <60 seconds for 3–5 PDFs
- ⚡ Future-ready architecture: modular, extensible, and production-friendly


git remote add origin https://github.com/vihsal09dream/adobe-hackathon-challenge-1b.git