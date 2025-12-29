from fastapi import FastAPI, Request
import os

app = FastAPI()

# Simple in-memory state
symbol_state = {}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    msg = data.get("message", "")

    if msg.startswith("ENABLE|"):
        sym = msg.split("|")[1]
        symbol_state[sym] = True
        return {"status": f"{sym} enabled"}

    if msg.startswith("DISABLE|"):
        sym = msg.split("|")[1]
        symbol_state[sym] = False
        return {"status": f"{sym} disabled"}

    symbol = data.get("symbol")
    if not symbol_state.get(symbol, False):
        return {"status": "blocked"}

    return {"status": "trade allowed"}
