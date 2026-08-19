# DocuMind AI

DocuMind AI is a Generative AI-based document assistant that allows users to upload documents and ask questions about their content. The application uses Retrieval-Augmented Generation (RAG) to find relevant information from the uploaded document and generate answers using the Google Gemini API.

## Live Demo

[Open DocuMind AI](https://documind-ai-jak3wc5gkhrgjflnddgepu.streamlit.app/)

## GitHub Repository

[View Source Code](https://github.com/ThanusriVentrapragada/DocuMind-AI)

## About the Project

Reading and searching through large documents can take a lot of time. DocuMind AI is designed to make this process easier by allowing users to interact with their documents through a simple question-and-answer interface.

Instead of manually searching through a document, users can upload it and ask questions in natural language. The system retrieves the most relevant parts of the document and uses the Gemini model to generate a response.

## Features

* Upload documents through the Streamlit interface
* Extract and process document content
* Split text into smaller chunks for efficient retrieval
* Retrieve relevant information based on the user's question
* Generate answers using Google Gemini
* Interactive question-answering interface
* Simple and easy-to-use web interface
* Deployed using Streamlit Cloud

## How It Works

```text
User uploads a document
        ↓
Document text is extracted
        ↓
Text is divided into smaller chunks
        ↓
Relevant information is stored for retrieval
        ↓
User asks a question
        ↓
Relevant document content is retrieved
        ↓
Google Gemini generates the response
        ↓
Answer is displayed to the user
```

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Generative AI
* Retrieval-Augmented Generation (RAG)
* Natural Language Processing
* Vector-based retrieval
* Git and GitHub

## Project Structure

```text
DocuMind-AI/
│
├── app.py
├── rag.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

Make sure Python is installed on your system.

You will also need a Google Gemini API key to run the application.

### Clone the Repository

```bash
git clone https://github.com/ThanusriVentrapragada/DocuMind-AI.git
```

Move into the project directory:

```bash
cd DocuMind-AI
```

### Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### Configure the API Key

The application requires a Google Gemini API key.

For local development, configure the API key using your preferred secure method.

For Streamlit Cloud, add the API key through the application's **Secrets** settings.

Do not upload API keys, passwords, or other sensitive information to GitHub.

### Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will then be available in your local browser.

## Example Use Cases

DocuMind AI can be useful for:

* Asking questions about study materials
* Finding specific information in documents
* Quickly understanding lengthy documents
* Research and academic document analysis
* Building AI-powered document assistants

## Future Improvements

Some improvements that can be added in future versions include:

* Support for multiple documents at the same time
* Conversation history
* Improved document retrieval
* Document summarization
* Voice-based interaction
* User authentication
* Support for additional document formats

## Deployment

The application is deployed using Streamlit Cloud and can be accessed through the live demo:

https://documind-ai-jak3wc5gkhrgjflnddgepu.streamlit.app/

## Author

**Thanusri Ventrapragada**

B.Tech – Electronics and Communication Engineering

## Project Highlights

This project helped me gain practical experience in:

* Generative AI
* Retrieval-Augmented Generation
* Prompt Engineering
* Natural Language Processing
* Python
* API Integration
* Streamlit
* Git and GitHub
* Cloud Deployment
