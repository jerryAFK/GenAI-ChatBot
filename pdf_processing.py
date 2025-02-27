import fitz  # PyMuPDF

def extract_text_from_pdfs(uploaded_files):
    """Extract text from multiple PDFs."""
    all_text = ""
    for pdf in uploaded_files:
        doc = fitz.open(stream=pdf.read(), filetype="pdf")
        for page in doc:
            all_text += page.get_text() + "\n\n"
    return all_text
