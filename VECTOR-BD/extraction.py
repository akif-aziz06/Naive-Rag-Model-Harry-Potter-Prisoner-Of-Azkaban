import PyPDF2

def extract_text_from_pdf(file_path):
    """Reads a PDF and returns the text as a single string."""
    pdf_text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                pdf_text += extracted + "\n"
    return pdf_text