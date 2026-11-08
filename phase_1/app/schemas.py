from pydantic import BaseModel

class PayloadRequest(BaseModel):
    montant: int
    volume_passees: float
    commission: float
    destination_country: str

class PayloadResponse(BaseModel):
    abandon_prob: float
    decision: bool