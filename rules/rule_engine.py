RULES = [
    {"name":"High Value Invoice","condition":lambda d: d.get("total_amount",0) > 10000,"severity":"HIGH"},
    {"name":"Missing Vendor","condition":lambda d: not d.get("vendor_name"),"severity":"MEDIUM"}
]

def evaluate_rules(data: dict):
    return [r for r in RULES if r["condition"](data)]
