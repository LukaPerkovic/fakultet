import io
import logging

from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from PIL import Image
from transformers import pipeline


# image_to_text("https://ankur3107.github.io/assets/images/image-captioning-example.png")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

logger.info("Loading the model...")
model = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
logger.info("Model loaded succesfully!")


@app.post("/generate/")
async def generate(file: str):
    logger.info("Received a generation request.")

    logger.info("Image loaded successfully.")

    result = model(file)
    logger.info("Inference completed.")

    return result
