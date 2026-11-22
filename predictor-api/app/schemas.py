from typing import Literal
from pydantic import BaseModel, Field

class ClientEntree(BaseModel):
    anciennete_mois: int = Field(ge=0, le=100)
    contrat: Literal["mensuel", "1_an", "2_ans"]
    facture_mensuelle: float = Field(gt=0, le=500)
    type_internet: Literal["aucun", "dsl", "fibre"]
    moyen_paiement: Literal["carte", "virement", "cheque"]
    senior: bool
    support_technique: bool
