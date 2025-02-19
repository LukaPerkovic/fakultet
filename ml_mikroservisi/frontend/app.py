import streamlit as st
import requests
import os
import logging
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv, find_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    ENV = os.environ["ENVIRONMENT"]
except KeyError:
    logger.warning("ENV variable not available. Trying to use local environment...")
    load_dotenv(find_dotenv())
    ENV = os.getenv("ENVIRONMENT", "DEV")

logger.info(f"Current environment set as: {ENV}")

host = "backend-service" if ENV == "PROD" else "localhost:7860"
endpoint = "transform"

backend_url = f"http://{host}/{endpoint}"

st.title("Aplikacija: Titlovanje slike")
st.write("**Ime:** Luka Perkovic")
st.write("**Broj indeksa:** 2023410428")
st.write("\n\n")
st.write("\n\n")


image_url = st.text_input("Unesi URL slike (http ili https)")

if image_url:
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))

        col1, col2 = st.columns(2)

        with col1:
            st.image(image, caption="Loaded Image", use_container_width=True)

        st.write("")
        st.write("Obrada...")

        # Send the image URL to the backend service
        response = requests.post(backend_url, json={"image_url": image_url})

        if response.status_code == 200:
            result = response.json()
            with col2:
                st.write("Prediction Results:")
                st.write(result[0].get("generated_text"))
        else:
            st.write("Error: Unable to get prediction results")

    except requests.exceptions.RequestException as e:
        st.write(f"Unable to fetch image from URL.")