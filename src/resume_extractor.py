import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("../data/CVs1/C1061.pdf")
    print(resume_text)
