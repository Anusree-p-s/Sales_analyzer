📊 RAG Sales Data Analyzer: ChromaDB + Gemini
This project is a Streamlit application designed to perform Retrieval-Augmented Generation (RAG) on internal PDF sales reports. It allows users to upload a proprietary sales report, embed the document chunks into a Chroma vector database using Google's powerful gemini-embedding-001, and then query the data using the Gemini 2.5 Flash model.

The application not only retrieves and synthesizes information but also includes a feature to automatically extract and visualize key financial distributions (like regional sales) as a custom-colored pie chart.

✨ Features
Secure Document Ingestion: Upload PDF files for processing.

Vector Database: Uses ChromaDB for efficient storage and retrieval of document chunks.

Google Embeddings: Leverages the high-quality Gemini Embedding model (gemini-embedding-001) for semantic search.

Gemini AI Q&A: Answers complex questions using the Gemini 2.5 Flash model based only on the retrieved document context.

Dynamic Visualization: Automatically identifies and plots numeric distributions (e.g., regional sales breakdown) into a customizable matplotlib pie chart.
