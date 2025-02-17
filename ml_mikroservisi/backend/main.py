import os
import logging
from pydantic import BaseModel
import requests
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


try:
    ENV = os.environ["ENVIRONMENT"]
except KeyError:
    logger.warning("ENV variable not available. Trying to use local environment...")
    load_dotenv()
    ENV = os.getenv("ENVIRONMENT", "DEV")

logger.info(f"Current environemnt set as: {ENV}")

app = FastAPI()

model_service = "model-service" if ENV == "PROD" else "localhost"
model_port = 5000
model_endpoint = "generate"

frontend_service = "frontend-service" if ENV == "PROD" else "localhost"
frontend_port = 8501
frontend_endpoint = ""


class FilePathRequest(BaseModel):
    file_path: str


# POST request from Frontend, with redirection of POST request to model
@app.post("/transform")
async def generate(request: FilePathRequest):
    file_path = request.file_path
    logger.info(f"Received file path: {file_path}")

    # Forward the file path to the model service
    response = requests.post(
        f"http://{model_service}:{model_port}/{model_endpoint}",
        json={"path": file_path},
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(
            status_code=response.status_code, detail="Error in model service"
        )
