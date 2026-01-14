from datetime import datetime

def validate_fields(data: dict) -> dict:
    results = {}
    results["invoice_number"] = bool(data.get("invoice_number"))
    try:
        datetime.strptime(data.get("invoice_date",""), "%m/%d/%Y")
        results["invoice_date"] = True
    except:
        results["invoice_date"] = False
    results["total_amount"] = data.get("total_amount",0) > 0
    return results
