def calculate_confidence(validation: dict) -> float:
    return round(sum(validation.values()) / len(validation), 2)
