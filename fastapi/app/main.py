from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session, init_db
from app.models import StockPrediction, StockPredictionCreate

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"ping": "pong"}

@app.get("/predict/stocks", response_model=list[StockPrediction])
async def get_stock_predictions(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(StockPrediction))
    stockpredictions = result.scalars().all()
    return [StockPrediction(ticker=stockprediction.ticker, forecast=stockprediction.forecast, id=stockprediction.id) for stockprediction in stockpredictions]


@app.post("/predict/stocks")
async def add_stock_prediction(stockprediction: StockPredictionCreate, session: AsyncSession = Depends(get_session)):
    stockprediction = StockPrediction(ticker=stockprediction.ticker, forecast=stockprediction.forecast)
    session.add(stockprediction)
    await session.commit()
    await session.refresh(stockprediction)
    return stockprediction
