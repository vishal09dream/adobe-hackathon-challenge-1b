from utils import extract_sections

def run_challenge(input_path, pdf_folder):
    import json

    with open(input_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    persona = config.get("persona", "")
    objective = config.get("objective", "")

    output = extract_sections(pdf_folder, persona, objective)
    return output
