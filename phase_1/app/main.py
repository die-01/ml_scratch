from fastapi import FastAPI
from app.schemas import PayloadRequest, PayloadResponse
import pandas as pd
from train import model
from app.config import THRESHOLD
from app.db import sessionLocal, Prediction, lifespan

app = FastAPI(lifespan=lifespan)

@app.post('/predict/', response_model=PayloadResponse)
async def predict_abandon(payload: PayloadRequest):
    data = payload.model_dump()

    df = pd.DataFrame([data])
    abandon_prob = float(model.predict_proba(df)[0][1])

    decision = abandon_prob >= THRESHOLD

    async with sessionLocal() as session:
        session.add(Prediction(**data, abandon_prob=abandon_prob, decision=decision))
        await session.commit()

    return PayloadResponse(abandon_prob=abandon_prob, decision=decision)
