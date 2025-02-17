import logging

from fastapi import FastAPI
from pydantic import BaseModel

from transformers import pipeline


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FilePath(BaseModel):
    path: str


app = FastAPI()

logger.info("Loading the model...")
model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
logger.info("Model loaded succesfully!")


@app.post("/generate")
async def generate(request: FilePath):
    logger.info("Received a generation request.")

    logger.info(f"File path received: {request.path}")

    result = model(request.path)
    logger.info("Inference completed.")
    return result
