from extraction.classifier import classify_document
from extraction.llm_extractor import extract_structured_data
from extraction.validator import validate_fields
from extraction.confidence import calculate_confidence
from rules.rule_engine import evaluate_rules

def run_langchain_pipeline(text: str):
    doc_type = classify_document(text)
    structured = extract_structured_data(text)
    validation = validate_fields(structured)
    confidence = calculate_confidence(validation)
    rules = evaluate_rules(structured)
    structured.update({
        "document_type": doc_type,
        "confidence_score": confidence,
        "rule_violations": rules
    })
    return structured
