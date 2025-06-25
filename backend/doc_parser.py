import pdfplumber
import docx


def extract_text_from_file(filepath):
    if filepath.endswith(".pdf"):
        return extract_pdf_text(filepath)
    elif filepath.endswith(".docx"):
        return extract_docx_text(filepath)
    else:
        raise ValueError("Unsupported file type")


def extract_pdf_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_docx_text(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])
