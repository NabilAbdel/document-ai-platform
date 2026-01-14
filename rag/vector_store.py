from langchain.vectorstores import FAISS
from langchain.embeddings import VertexAIEmbeddings

def build_store(texts):
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    return FAISS.from_texts(texts, embeddings)
