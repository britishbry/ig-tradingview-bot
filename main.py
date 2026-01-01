from fastapi import FastAPI
from typing import Dict
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/webhook")
async def webhook(payload: Dict):
    logging.info("WEBHOOK RECEIVED")
    logging.info(payload)
    return {"status": "ok"}
