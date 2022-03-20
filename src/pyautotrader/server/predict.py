from fastapi import FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from pyautotrader.models.entities import QuoteORM


def get_predict_from_db(exchange, asset, timeframe, date, time, parameters, engine):
    if parameters['CURRENT_TIMEFRAME'] != timeframe:
        raise HTTPException(
            status_code=500, detail=f"ERROR! The requested data timeframe was {timeframe}, but the server is serving:{parameters['CURRENT_TIMEFRAME']} data")

    with Session(engine) as session:
        final_datetime = ((int(date) * 10000) + int(time)) - 201600000000
        result = session.query(QuoteORM).filter(QuoteORM.exchange == exchange).filter(
            QuoteORM.asset == asset).filter(QuoteORM.timeframe == timeframe).filter(
                QuoteORM.datetime <= final_datetime).order_by(desc(QuoteORM.datetime)).limit(300).all()
        res = []
        for row in result:
            res.append({
                'exchange': row.exchange,
                'asset': row.asset,
                'timeframe': row.timeframe,
                'date': row.date,
                'time': row.time,
                'open': row.open,
                'high': row.high,
                'low': row.low,
                'close': row.close,
                'business': row.business,
                'volume': row.volume
            })

        session.commit()

    res.reverse()

    return {'rows': res}
