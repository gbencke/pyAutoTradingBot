from fastapi import FastAPI, HTTPException


def get_predict_from_db(exchange, asset, timeframe, date, time, model):
    if model['CURRENT_TIMEFRAME'] != timeframe:
        raise HTTPException(
            status_code=500, detail=f"ERROR! The requested data timeframe was {timeframe}, but the server is serving:{model['CURRENT_TIMEFRAME']} data")
    return {}
