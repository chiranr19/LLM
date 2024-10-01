Chainlit-GCP-VertexAI RAG System
This repository contains code that enables users to upload files via a Chainlit interface, store those files in Google Cloud Storage (GCS), and leverage Vertex AI Embeddings and Chroma DB for retrieval-augmented generation (RAG). This allows users to ask questions related to the contents of the uploaded files.

Key Components
Chainlit: Provides an interactive interface for users to upload files and interact with the system.
Google Cloud Storage (GCS): Used to store the uploaded files.
Vertex AI Embeddings: Embeds the contents of the files into vector representations for retrieval.
Chroma DB: A vector database used for storing and searching document embeddings.
Retrieval-Augmented Generation (RAG): Allows users to ask questions about the uploaded files and retrieves the most relevant information.
Features
File Upload: Users can upload a file (e.g., a PDF) through the Chainlit interface.
GCS Integration: The file is uploaded to a specified Google Cloud Storage bucket.
Vector Embeddings: The contents of the file are embedded using Google Vertex AI Embeddings and stored in Chroma DB.
RAG for Q&A: Users can ask questions, and the system retrieves relevant information from the uploaded file using Retrieval-Augmented Generation.
Prerequisites
Python 3.10+
Chainlit: An interactive chatbot interface.
Google Cloud SDK: Set up for accessing GCS and Vertex AI.
Chroma DB: A vector database.
OpenAI API: For natural language processing tasks.
