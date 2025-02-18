FROM python:3.10-slim

WORKDIR /app

ENV ENVIRONMENT="PROD"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]