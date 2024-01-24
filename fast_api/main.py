from  fastapi import FastAPI
import os

DEVELOPMENT = os.getenv("DEVELOPMENT")

app = FastAPI()

@app.get("/")
def root():
    return {
        "api_version": "1.0",
        "status": "success",
        "staging": "development" if DEVELOPMENT else "production",
        "message": "Root API endpoint",
        "data": []
  }