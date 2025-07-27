from pathlib import Path
import fitz  # PyMuPDF
from onnxruntime import InferenceSession
from transformers import AutoTokenizer
import numpy as np

# Load tokenizer and ONNX model (assume files are present locally)
tokenizer = AutoTokenizer.from_pretrained("Xenova/all-MiniLM-L6-v2", local_files_only=True)
session = InferenceSession("model.onnx", providers=["CPUExecutionProvider"])

def get_embedding(text):
    tokens = tokenizer(text, return_tensors="np", padding=True, truncation=True)
    inputs = {k: v for k, v in tokens.items()}
    output = session.run(None, inputs)
    return output[0][0]  # embedding vector

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def extract_sections(pdf_folder: Path, persona: str, objective: str):
    results = []

    # Combine persona and objective for query embedding
    query_text = f"{persona} {objective}"
    query_emb = get_embedding(query_text)

    for pdf_file in sorted(pdf_folder.glob("*.pdf")):
        doc = fitz.open(pdf_file)
        full_text = " ".join([page.get_text() for page in doc])
        doc.close()

        # Get embedding for document
        doc_emb = get_embedding(full_text)
        score = cosine_similarity(query_emb, doc_emb)

        results.append({
            "file": pdf_file.name,
            "best_section": full_text[:300],  # top 300 chars
            "score": round(score, 2)
        })

    return results
