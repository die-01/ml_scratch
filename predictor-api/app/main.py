from fastapi import FastAPI

from app.schemas import ClientEntree

app = FastAPI(title="Predictor API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(client: ClientEntree):
    return {"received_data": client.dict()}

