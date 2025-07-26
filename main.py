import fitz  
import os
import json
import pymupdf

def get_heading_level(font_size):
    if font_size >= 18:
        return "H1"
    elif font_size >= 14:
        return "H2"
    elif font_size >= 12:
        return "H3"
    return None

def process_pdf(file_path):
    doc = fitz.open(file_path)
    title_candidate = {"text": "", "size": 0}
    outline = []

    for page_number, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text or len(text.split()) > 12:
                        continue  

                    font_size = span["size"]

                    if font_size > title_candidate["size"]:
                        title_candidate = {"text": text, "size": font_size}

                    level = get_heading_level(font_size)
                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_number
                        })

    return {
        "title": title_candidate["text"],
        "outline": outline
    }

def main():
    input_dir = "./input"
    output_dir = "./output"

    filename = "sample3.pdf"

    file_path = os.path.join(input_dir, filename)

    if not os.path.exists(file_path):
        print(f"❌ File '{filename}' not found in 'input' folder.")
        return

    result = process_pdf(file_path)
    output_filename = filename.replace(".pdf", ".json")

    with open(os.path.join(output_dir, output_filename), "w", encoding="utf-8") as out_file:
        json.dump(result, out_file, indent=2, ensure_ascii=False)

    print(f"✅ JSON saved to: output/{output_filename}")

if __name__ == "__main__":
    main()
