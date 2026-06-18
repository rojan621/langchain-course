import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_chroma import Chroma

load_dotenv()

if __name__ == '__main__':
    print("Ingesting...")
    loader = TextLoader("./mediumblog1.txt")
    document = loader.load()

    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"created {len(texts)} chunks")

    embeddings = OllamaEmbeddings(model="qwen2.5:7b")

    print("ingesting...")
    Chroma.from_documents(documents=texts,
                          embedding=embeddings,
                          persist_directory="./chroma_db")
    print("finish")
    

