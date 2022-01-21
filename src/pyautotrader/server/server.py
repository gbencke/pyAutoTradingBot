import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ok, worked!"}


def start_server(args):
    uvicorn.run("pyautotrader.server:app", host="127.0.0.1",
                port=5000, log_level="info")
