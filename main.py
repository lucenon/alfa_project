from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from app.model_service import load_artifacts, predict
from app.schemas import Input, Output
from app.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_artifacts()
    logger.info("Model loaded")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict", response_model=Output)
def predict_route(data: Input):
    try:
        logger.info("Get request")
        result = predict(data.text)
        logger.info(f"Result: {result}")
        return result
    except Exception as e:
        logger.error(f"Inference error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

