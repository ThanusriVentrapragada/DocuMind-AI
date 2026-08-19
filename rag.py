from document_processor import extract_text_from_pdf, chunk_text
from embeddings import create_embeddings
from vector_store import VectorStore
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

vector_store = VectorStore()


def process_document(file):
    text = extract_text_from_pdf(file)

    if not text.strip():
        return False

    chunks = chunk_text(text)

    if not chunks:
        return False

    embeddings = create_embeddings(chunks)

    vector_store.add(chunks, embeddings)

    return True


def answer_question(question):
    if not vector_store.chunks:
        return "Please upload a document first."

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )

    query_embedding = response.embeddings[0].values

    results = vector_store.search(
        query_embedding,
        top_k=3
    )

    context = "\n\n".join(
        result["chunk"] for result in results
    )

    prompt = f"""
You are DocuMind AI, an AI assistant that answers questions based on uploaded documents.

Use only the information provided in the context below.

If the answer is not available in the context, say:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text