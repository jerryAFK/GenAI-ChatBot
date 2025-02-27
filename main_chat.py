import streamlit as st
from pdf_processing import extract_text_from_pdfs
from vector_store import store_pdf_embeddings
from qa_system import ask_question

st.set_page_config(page_title="📄 GenAI of learning", page_icon="🤖🤓")

st.title("📄 Upload PDFs of you subject and start learning :)")
st.write("Upload and I'll be you teacher!")

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload Subject PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    st.info("📄 Processing PDFs... Please wait!")
    
    # Extract text from all uploaded PDFs
    text = extract_text_from_pdfs(uploaded_files)

    # Store in vector database
    vector_store = store_pdf_embeddings(text)
    st.success("✅ PDFs processed successfully!")

    # User query
    query = st.text_input("What you want to learn ?, ask away!")
    
    if query:
        response = ask_question(vector_store, query)
        st.write("🤖 AI:", response)
