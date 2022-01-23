import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from .model.post_value_objects import Quote

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Ok, worked!"}


@app.post("/quotes/{exchange}/{asset}/{timeframe}/")
async def post_quote(exchange: str, asset: str, timeframe: str, quote: Quote):
    if timeframe not in ['5Min', '15Min', '30Min', '60Min', 'Daily']:
        raise HTTPException(
            status_code=400, detail='timeframe should be:5Min, 15Min, 30Min, 60Min, Daily')

    print(f"Exchange:{exchange}")
    print(f"Asset:{asset}")
    print(f"TimeFrame:{timeframe}")
    print(str(quote))


def start_server(args):
    CURRENT_IP = "127.0.0.1"
    CURRENT_PORT = 5000

    if args.sqlalchemy_connection_string is None:
        print('In order to start the server, you need to specify the SQLAlchemy connection string...')
        sys.exit(1)
    if args.server_port is not None:
        CURRENT_PORT = args.server_port
    if args.listening_ip is not None:
        CURRENT_IP = args.listening_ip

    uvicorn.run("pyautotrader.server:app", host=CURRENT_IP,
                port=CURRENT_PORT, log_level="debug")
