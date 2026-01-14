from langchain_openai import ChatOpenAI
from extraction.schema import InvoiceSchema
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def extract_structured_data(text: str) -> dict:
    response = llm.invoke(text[:3000])
    return InvoiceSchema(**json.loads(response.content)).dict()
