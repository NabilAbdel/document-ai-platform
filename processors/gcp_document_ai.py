from google.cloud import documentai_v1 as documentai
import os

def extract_with_document_ai(file_path: str) -> str:
    client = documentai.DocumentProcessorServiceClient()
    name = f"projects/{os.getenv('GCP_PROJECT_ID')}/locations/us/processors/{os.getenv('DOC_AI_PROCESSOR_ID')}"
    with open(file_path, "rb") as f:
        raw_document = {"content": f.read(), "mime_type": "application/pdf"}
    result = client.process_document(request={"name": name, "raw_document": raw_document})
    return result.document.text
