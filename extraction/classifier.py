from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def classify_document(text: str) -> str:
    return llm.invoke(text[:2000]).content.strip().lower()
