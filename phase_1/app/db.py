import joblib
from contextlib import asynccontextmanager

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fastapi import FastAPI
from app.config import DATABASE_URL

class Base(DeclarativeBase):
    pass

class Prediction(Base):
    __tablename__ = "predictions"
    id: Mapped[int] = mapped_column(primary_key=True)
    montant: Mapped[int]
    volume_passees: Mapped[float]
    commission: Mapped[float]
    destination_country: Mapped[str]
    abandon_prob: Mapped[float]
    decision: Mapped[bool]

engine = create_async_engine(DATABASE_URL)

sessionLocal = async_sessionmaker(engine, expire_on_commit=False)

model = joblib.load("model.joblib")

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)