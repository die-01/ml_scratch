# creating the model of the payload
# creating the model/structure of the table of the database

# getting the JSON payload through a "get" method
# verifying the payload with pydantic
# passing the payload to the model
# initializing the database
# getting the result and adding the result and the input metrics to an instance of the DB
# sending the result in a "post" method





from pydantic import BaseModel

class PayloadRequest(BaseModel):
    montant: int
    volume_passees: float
    commission: float
    destination_country: int

class PayloadResponse(BaseModel):
    abandon_prob: float
    decision: bool
