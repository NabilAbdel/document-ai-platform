from pydantic import BaseModel
from typing import Optional

class InvoiceSchema(BaseModel):
    document_type: str = "invoice"
    invoice_number: Optional[str]
    invoice_date: Optional[str]
    vendor_name: Optional[str]
    total_amount: Optional[float]
