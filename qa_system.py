import requests
import os

# Set your Groq API Key
GROQ_API_KEY = "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"

def ask_question(vector_store, query):
    """Retrieves context from PDFs and queries Groq API."""

    # Retrieve relevant document context
    retrieved_docs = vector_store.as_retriever().get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in retrieved_docs])[:2000]  # Limit context size

    # Prepare API request
    api_url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}

    payload = {
        "model": "llama3-8b-8192",  # ✅ Use a supported Groq model
        "messages": [
            {"role": "system", "content": "Answer questions based on the given context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ],
        "temperature": 0.5,
        "max_tokens": 512
    }

    # Send API request
    response = requests.post(api_url, headers=headers, json=payload)

    # Handle response
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"API Error: {response.json()}"
