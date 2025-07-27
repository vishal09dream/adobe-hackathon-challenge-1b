from pathlib import Path
from process import run_challenge

BASE_PATH = Path("/app/Challenge_1b")
collections = sorted([d for d in BASE_PATH.iterdir() if d.is_dir()])

for collection in collections:
    input_path = collection / "challenge1b_input.json"
    output_path = collection / "challenge1b_output.json"
    pdf_folder = collection / "PDFs"

    if input_path.exists() and pdf_folder.exists():
        print(f"✅ Processing: {collection.name}")
        result = run_challenge(input_path, pdf_folder)
        with open(output_path, "w", encoding="utf-8") as f:
            import json
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"✅ Output written: {output_path.name}")
    else:
        print(f"⚠️ Skipping {collection.name} (Missing input or PDFs)")
