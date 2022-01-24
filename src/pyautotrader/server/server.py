import sys
import uvicorn
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .value_objects import Quote
from pyautotrader.models.entities import QuoteORM

app = FastAPI()
engine = None


@app.get("/")
async def root():
    return {"message": "Ok, worked!"}


@app.post("/quotes/{exchange}/{asset}/{timeframe}/")
async def post_quote(exchange: str, asset: str, timeframe: str, quote: Quote):
    if timeframe not in ['5Min', '15Min', '30Min', '60Min', 'Daily']:
        raise HTTPException(
            status_code=400, detail='timeframe should be:5Min, 15Min, 30Min, 60Min, Daily')

    quote_to_add = QuoteORM(exchange=exchange,
                            asset=asset,
                            timeframe=timeframe,
                            date=quote.date,
                            time=quote.time,
                            open=quote.open,
                            high=quote.high,
                            low=quote.low,
                            close=quote.close,
                            business=quote.business,
                            volume=quote.volume)

    try:
        with Session(engine) as session:
            session.add(quote_to_add)
            session.commit()
    except IntegrityError as ex:
        raise HTTPException(status_code=500, detail=str(ex))


def start_server(args):
    global engine

    CURRENT_IP = "127.0.0.1"
    CURRENT_PORT = 5000

    if args.sqlalchemy_connection_string is None:
        print('In order to start the server, you need to specify the SQLAlchemy connection string...')
        sys.exit(1)
    if args.server_port is not None:
        CURRENT_PORT = args.server_port
    if args.listening_ip is not None:
        CURRENT_IP = args.listening_ip

    engine = create_engine(args.sqlalchemy_connection_string)

    uvicorn.run("pyautotrader.server:app", host=CURRENT_IP,
                port=CURRENT_PORT, log_level="debug")
