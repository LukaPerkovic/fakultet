import streamlit as st
import requests
import os
import tempfile
import logging

from dotenv import load_dotenv, find_dotenv


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


try:
    ENV = os.environ["ENVIRONMENT"]
except KeyError:
    logger.warning("ENV variable not available. Trying to use local environment...")
    load_dotenv(find_dotenv())
    ENV = os.getenv("ENVIRONMENT", "DEV")

logger.info(f"Current environemnt set as: {ENV}")

host = "backend-service" if ENV == "PROD" else "localhost"
port = 7860
endpoint = "transform"

backend_url = f"http://{host}:{port}/{endpoint}"

st.title("Image Upload and Prediction")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["jpg", "jpeg", "png"], key="unique_file_uploader"
)

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    st.image(temp_file_path, caption="Uploaded Image", use_container_width=True)
    st.write("")
    st.write("Classifying...")

    # Send the temporary file path to the backend service
    response = requests.post(backend_url, json={"file_path": temp_file_path})

    if response.status_code == 200:
        result = response.json()
        st.write("Prediction Results:")
        st.write(result[0].get("generated_text"))
    else:
        st.write("Error: Unable to get prediction results")

    # Clean up the temporary file
    os.remove(temp_file_path)
