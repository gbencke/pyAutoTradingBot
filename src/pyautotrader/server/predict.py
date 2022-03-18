from fastapi import FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from pyautotrader.models.entities import QuoteORM


def get_predict_from_db(exchange, asset, timeframe, date, time, parameters, engine):
    if parameters['CURRENT_TIMEFRAME'] != timeframe:
        raise HTTPException(
            status_code=500, detail=f"ERROR! The requested data timeframe was {timeframe}, but the server is serving:{parameters['CURRENT_TIMEFRAME']} data")

    with Session(engine) as session:
        result = session.query(QuoteORM).filter(QuoteORM.exchange == exchange).filter(
            QuoteORM.asset == asset).filter(QuoteORM.timeframe == timeframe).filter(QuoteORM.date <= date).order_by(desc(QuoteORM.date))
        res = []
        final_datetime = int(date) * 1000 + int(time)
        for row in result:
            if final_datetime < ((int(row.date) * 1000) + int(row.time)):
                continue

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
            if len(res) == 500:
                break

        session.commit()

    res.reverse()

    return {'rows': res}
