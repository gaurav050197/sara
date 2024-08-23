from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/intro",tags=["1 part"])
async def root() ->dict:
    return{"ping":"pong"}

if __name__ == "__main__":
    uvicorn.run("main3:app", host="127.0.0.2", port=8001, reload=True)
