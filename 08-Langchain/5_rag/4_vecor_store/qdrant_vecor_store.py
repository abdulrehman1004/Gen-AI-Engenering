# Install Some Packages ( langchain-qdrant langchain-pinecone pinecone-notebooks )
# Import Packages

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain_qdrant import QdrantVectorStore


# Load the PDF document using PyPDFLoader
load_data = PyPDFLoader(
    "https://dvikan.no/ntnu-studentserver/kompendier/artificial-intelligence-agents-and-environments.pdf")

pages = load_data.load()
# print(len(pages))
# print(pages[50])

# Split the document into chunks using Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size="2000",
    chunk_overlap="200"
)

# MetaData Processing:
# Create an empty list to store processed document chunks
doc_list = []

# Iterate over each page in the extracted pages
for page in pages:

    # Split the page content into smaller chunks
    pg_split = text_splitter.split_text(page.page_content)
    
    doc_list.append(pg_split)

    # # Iterate over each chunk and create Document objects
    # for pg_sub_split in pg_split:

    #     # Metadata for each chunk, including source and page number
    #     metadata = {"source": "artificial-intelligence-agents-and-environments.pdf",
    #                 "page_no": page.metadata["page"] + 1}

    #     # Create a Document object with content and metadata
    #     doc_string = Document(page_content=pg_sub_split, metadata=metadata)

    #     # Append the Document object to the list
    #     doc_list.append(doc_string)

print(len(doc_list))
# =========================== Create and Add Embedding to the Qdrant Vector Store  ===========================
# Initialize HuggingFace Embedding Model

# ========== Create Embedding using HuggingFace Model ==========

# Initialize Google Embedding Model

# ========== Create Embedding using Google Gemini Model ==========
