Q-Creator: Automated PDF to Q&A Generator
Q-Creator is a web application that leverages the power of Google's Gemini API and LangChain to automatically generate a set of questions and answers from an uploaded PDF document. This tool is perfect for creating study guides, summarizing complex documents, or generating FAQs from technical manuals.

The application provides a clean user interface to upload a file, view the generated Q&A pairs, and download them as a CSV file for offline use.

!

Features
PDF Upload: Simple drag-and-drop or file-picker interface for uploading PDF documents.

Automated Q&A Generation: Intelligently creates relevant questions and generates accurate answers based on the document's content.

Web-Based Visualization: Displays the generated question-answer pairs in a clean, easy-to-read card format.

CSV Export: Allows users to download the full Q&A list as a CSV file.

RAG Pipeline: Uses a Retrieval-Augmented Generation (RAG) approach with a FAISS vector store for high-quality, context-aware answers.

Technology Stack
Backend: FastAPI

AI Framework: LangChain

LLM & Embeddings: Google Gemini API (gemini-pro, embedding-001)

Vector Store: FAISS (Facebook AI Similarity Search)

Frontend: HTML, Tailwind CSS, JavaScript

Setup and Installation Guide
Follow these steps to set up and run the project on your local machine.

Step 1: Clone the Repository
First, clone the project from GitHub to your local system.

git clone [https://github.com/viplavs2004/Q-Creator.git](https://github.com/viplavs2004/Q-Creator.git)
cd Q-Creator

Step 2: Create a Python Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Step 3: Install Required Libraries
Install all the necessary Python packages using the requirements.txt file.

pip install -r requirements.txt

(Note: If you don't have a requirements.txt file yet, you can create one by running pip freeze > requirements.txt after installing the packages manually.)

Step 4: Set Up Your Environment Variables
The application requires a Google API key to function.

Create a .env file in the root directory of the project.

Get your Google API Key. You can obtain one from the Google AI Studio.

Add your key to the .env file like this:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

How to Run the Application
Once the setup is complete, you can start the application using the FastAPI server.

Run the following command in your terminal from the project's root directory:

uvicorn app:app --reload

The server will start, and you can access the application by navigating to https://www.google.com/search?q=http://127.0.0.1:8000 in your web browser.

Usage
Open the Webpage: Go to http://127.0.0.1:8000.

Upload a PDF: Drag and drop a PDF file or click the upload area to select one from your computer.

Generate Q&A: Click the "Generate Q&A" button.

View Results: The application will process the document and display the generated question-answer pairs on the screen. This may take a few minutes for large documents.

Download: Once the processing is complete, a "Download CSV" button will appear, allowing you to save the results.