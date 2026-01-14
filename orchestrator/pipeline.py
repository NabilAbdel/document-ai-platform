from processors.gcp_document_ai import extract_with_document_ai
from orchestrator.langchain_pipeline import run_langchain_pipeline
import os

def run_pipeline(file_path: str):
    text = extract_with_document_ai(file_path)
    return run_langchain_pipeline(text)
