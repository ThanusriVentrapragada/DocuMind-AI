import streamlit as st
from dotenv import load_dotenv
from rag import process_document, answer_question
import os

load_dotenv()

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="📚",
    layout="wide"
)

if not os.getenv("GEMINI_API_KEY"):
    st.error("GEMINI_API_KEY is missing in .env")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

st.markdown(
    """
    <style>
    .title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        color: #777777;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .document-box {
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
        background-color: #f5f5f5;
        color: #222222;
    }

    [data-testid="stFileUploader"] {
        background-color: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 10px;
        padding: 10px;
    }

    [data-testid="stFileUploader"] section {
        background-color: #ffffff;
    }

    [data-testid="stFileUploader"] button {
        color: #222222 !important;
        background-color: #ffffff !important;
        border: 1px solid #cccccc !important;
    }

    [data-testid="stFileUploader"] small {
        color: #555555 !important;
    }

    [data-testid="stFileUploader"] label {
        color: #222222 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">📚 DocuMind AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Chat with your documents using AI</div>',
    unsafe_allow_html=True
)

with st.sidebar:

    st.header("📄 Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        for uploaded_file in uploaded_files:

            if uploaded_file.name not in st.session_state.processed_files:

                with st.spinner(
                    f"Processing {uploaded_file.name}..."
                ):

                    success = process_document(
                        uploaded_file
                    )

                if success:

                    st.session_state.processed_files.append(
                        uploaded_file.name
                    )

                    st.success(
                        f"{uploaded_file.name} uploaded"
                    )

                else:

                    st.error(
                        f"Could not process {uploaded_file.name}"
                    )

    st.divider()

    st.subheader("Uploaded Files")

    if st.session_state.processed_files:

        for file_name in st.session_state.processed_files:

            st.markdown(
                f'<div class="document-box">📄 {file_name}</div>',
                unsafe_allow_html=True
            )

    else:

        st.info("No documents uploaded.")

    st.divider()

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.caption(
        "DocuMind AI • RAG-based Document Assistant"
    )

if not st.session_state.messages:

    st.info(
        "👋 Upload a PDF and ask a question to get started."
    )

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )

question = st.chat_input(
    "Ask a question about your documents..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = answer_question(question)

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )