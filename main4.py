from fastapi import FastAPI
from fastapi.testclient import TestClient

app=FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "hellow world"}
