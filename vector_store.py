import os
import faiss
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Use a free, local embedding model 
def store_pdf_embeddings(text):
    """Convert extracted text into vector embeddings and store using FAISS."""
    
    # Use a free model for text embeddings (No API key needed)
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    
    # Convert text into vector embeddings
    vector_store = FAISS.from_texts([text], embeddings)
    
    return vector_store