import os
from datetime import datetime

import pandas_ta as ta
import pandas as pd
import joblib

from fastapi import FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from pyautotrader.models.entities import QuoteORM

model_to_use = None
best_short_booster = None
best_long_booster = None
predict_cache = {}


def get_slope(current_bar, value_to_calculate):
    return 0
    a = []
    b = []
    for current_x in range(0, 11):
        a.append(current_x)
        b.append(current_bar[f'x{current_x}_{value_to_calculate}'])
    return linregress(a, b).slope


def predict_short(row, current_parameters):
    global best_short_booster
    a = row[current_parameters['CURRENT_X_COLUMNS']].to_numpy().reshape(1, -1)
    return best_short_booster.get_booster().inplace_predict(a)[0]


def predict_long(row, current_parameters):
    global best_long_booster
    a = row[current_parameters['CURRENT_X_COLUMNS']].to_numpy().reshape(1, -1)
    return best_long_booster.get_booster().inplace_predict(a)[0]


def return_first_model(DATA_OUTPUT_DIR):
    files_found = [x for x in os.listdir(
        DATA_OUTPUT_DIR) if x.endswith('.pickle')]
    files_found_tokens = [x.split('.') for x in files_found]

    models_found = {}

    for current_model in files_found_tokens:
        model_name = '.'.join(current_model[:-2])
        filename = os.path.join(DATA_OUTPUT_DIR, '.'.join(current_model))
        if not model_name in models_found:
            models_found[model_name] = {}
        models_found[model_name][current_model[-2]] = filename

    return models_found[list(models_found.keys())[0]]


def get_predict_data_from_db(exchange, asset, timeframe, date, time, parameters, engine, DATA_OUTPUT_DIR):
    with Session(engine) as session:
        final_datetime = ((int(date) * 10000) + int(time)) - 201600000000
        result = session.query(QuoteORM).filter(QuoteORM.exchange == exchange).filter(
            QuoteORM.asset == asset).filter(QuoteORM.timeframe == timeframe).filter(
                QuoteORM.datetime <= final_datetime).order_by(desc(QuoteORM.datetime)).limit(250).all()
        data5Min = []
        for row in result:
            data5Min.append({
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

        result = session.query(QuoteORM).filter(QuoteORM.exchange == exchange).filter(
            QuoteORM.asset == asset).filter(QuoteORM.timeframe == 'Daily').filter(
                QuoteORM.datetime <= final_datetime).order_by(desc(QuoteORM.datetime)).limit(30).all()
        dataDaily = []
        for row in result:
            dataDaily.append({
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

        data5Min.reverse()
        dataDaily.reverse()

        session.commit()

    csv_5Min = pd.DataFrame(data5Min)
    csv_Daily = pd.DataFrame(dataDaily)

    return csv_5Min, csv_Daily


def calculate_ta(csv_5Min):
    csv_5Min['datetime'] = csv_5Min.apply(lambda x: datetime.strptime(
        str(x['date']) + ' ' + str(x['time']), '%Y%m%d %H%M'), axis=1)
    csv_5Min.set_index(pd.DatetimeIndex(csv_5Min["datetime"]), inplace=True)
    csv_5Min['ema9'] = csv_5Min.ta.ema(length=9)
    csv_5Min['ema21'] = csv_5Min.ta.ema(length=21)
    csv_5Min['ema55'] = csv_5Min.ta.ema(length=55)
    csv_5Min['ema144'] = csv_5Min.ta.ema(length=144)
    csv_5Min['ema233'] = csv_5Min.ta.ema(length=233)
    csv_5Min['vwap'] = csv_5Min.ta.vwap()
    return csv_5Min


def calculate_predict(generated_bars, parameters):
    df_current_total_dataset = pd.DataFrame(generated_bars)
    df_current_total_dataset['short_predict'] = df_current_total_dataset.apply(
        lambda row: predict_short(row, parameters), axis=1)
    df_current_total_dataset['long_predict'] = df_current_total_dataset.apply(
        lambda row: predict_long(row, parameters), axis=1)
    return df_current_total_dataset


def get_predict_from_db(exchange, asset, timeframe, date, time, parameters, engine, DATA_OUTPUT_DIR):
    global model_to_use
    global best_short_booster
    global best_long_booster
    global predict_cache

    if parameters['CURRENT_TIMEFRAME'] != timeframe:
        raise HTTPException(
            status_code=500, detail=f"ERROR! The requested data timeframe was {timeframe}, but the server is serving:{parameters['CURRENT_TIMEFRAME']} data")

    predict_key = f'{exchange}.{asset}.{timeframe}.{date}.{time}'
    if predict_key in predict_cache:
        return predict_cache[predict_key]

    csv_5Min, csv_Daily = get_predict_data_from_db(
        exchange, asset, timeframe, date, time, parameters, engine, DATA_OUTPUT_DIR)

    generated_bars = []

    csv_5Min = calculate_ta(csv_5Min)

    if DATA_OUTPUT_DIR is not None and False:
        test_data = os.path.join(DATA_OUTPUT_DIR, 'saida_test_data.xlsx')
        csv_5Min.to_excel(test_data)

    data_daily = csv_Daily.to_dict('records')
    data_5min = csv_5Min.to_dict('records')

    daily_dates = []
    ohlc_daily = {}

    index = len(data_5min) - 1

    for current_date in data_daily:
        ohlc_daily[current_date['date']] = current_date
        daily_dates.append(current_date['date'])

    current_date = data_5min[index]['date']
    current_time = data_5min[index]['time']

    current_open = data_5min[index]['open']
    current_volume = data_5min[index]['volume']

    previous_date = [x for x in daily_dates if x < current_date]
    previous_date = previous_date[len(previous_date)-1]
    previous_date = ohlc_daily[previous_date]

    current_bar = {}

    current_bar['current_open'] = current_open
    current_bar['current_date'] = current_date
    current_bar['current_time'] = current_time
    current_bar['current_bar_in_date'] = 0

    current_bar['previous_date'] = previous_date['date']
    current_bar['previous_high_real'] = previous_date['high']
    current_bar['previous_close_real'] = previous_date['close']
    current_bar['previous_low_real'] = previous_date['low']
    current_bar['previous_open_real'] = previous_date['open']
    current_bar['previous_high'] = (
        (previous_date['high'] / current_open) - 1) * 100
    current_bar['previous_close'] = (
        (previous_date['close'] / current_open) - 1) * 100
    current_bar['previous_low'] = (
        (previous_date['low'] / current_open) - 1) * 100
    current_bar['previous_open'] = (
        (previous_date['open'] / current_open) - 1) * 100

    current_bar['x0_vwap'] = (
        (data_5min[index-11]['vwap'] / current_open) - 1) * 100
    current_bar['x0_ema9'] = (
        (data_5min[index-11]['ema9'] / current_open) - 1) * 100
    current_bar['x0_ema21'] = (
        (data_5min[index-11]['ema21'] / current_open) - 1) * 100
    current_bar['x0_ema55'] = (
        (data_5min[index-11]['ema55'] / current_open) - 1) * 100
    current_bar['x0_ema144'] = (
        (data_5min[index-11]['ema144'] / current_open) - 1) * 100
    current_bar['x0_ema233'] = (
        (data_5min[index-11]['ema233'] / current_open) - 1) * 100
    current_bar['x0_ema9_real'] = data_5min[index-11]['ema9']
    current_bar['x0_ema21_real'] = data_5min[index-11]['ema21']
    current_bar['x0_ema55_real'] = data_5min[index-11]['ema55']
    current_bar['x0_ema144_real'] = data_5min[index-11]['ema144']
    current_bar['x0_ema233_real'] = data_5min[index-11]['ema233']
    current_bar['x0_open'] = (
        (data_5min[index-11]['open'] / current_open) - 1) * 100
    current_bar['x0_high'] = (
        (data_5min[index-11]['high'] / current_open) - 1) * 100
    current_bar['x0_low'] = (
        (data_5min[index-11]['low'] / current_open) - 1) * 100
    current_bar['x0_close'] = (
        (data_5min[index-11]['close'] / current_open) - 1) * 100
    current_bar['x0_volume'] = (
        (data_5min[index-11]['volume'] / current_volume) - 1) * 100
    current_bar['x0_open_real'] = data_5min[index-11]['open']
    current_bar['x0_high_real'] = data_5min[index-11]['high']
    current_bar['x0_low_real'] = data_5min[index-11]['low']
    current_bar['x0_close_real'] = data_5min[index-11]['close']
    current_bar['x0_height'] = current_bar['x0_high'] - current_bar['x0_low']
    current_bar['x0_body'] = ((max([current_bar['x0_open_real'],  current_bar['x0_close_real']]) /
                              min([current_bar['x0_open_real'],  current_bar['x0_close_real']])) - 1) * 100
    if current_bar['x0_open'] > current_bar['x0_close']:
        current_bar['x0_height'] *= -1
        current_bar['x0_body'] *= -1
    current_bar['x0_roc'] = (
        (current_bar['x0_open_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_ema9_close'] = (
        (current_bar['x0_ema9_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_ema21_close'] = (
        (current_bar['x0_ema21_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_ema55_close'] = (
        (current_bar['x0_ema55_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_ema144_close'] = (
        (current_bar['x0_ema144_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x0_ema233_close'] = (
        (current_bar['x0_ema233_real'] / current_bar['x0_close_real']) - 1) * 100

    current_bar['x1_vwap'] = (
        (data_5min[index-10]['vwap'] / current_open) - 1) * 100
    current_bar['x1_ema9'] = (
        (data_5min[index-10]['ema9'] / current_open) - 1) * 100
    current_bar['x1_ema21'] = (
        (data_5min[index-10]['ema21'] / current_open) - 1) * 100
    current_bar['x1_ema55'] = (
        (data_5min[index-10]['ema55'] / current_open) - 1) * 100
    current_bar['x1_ema144'] = (
        (data_5min[index-10]['ema144'] / current_open) - 1) * 100
    current_bar['x1_ema233'] = (
        (data_5min[index-10]['ema233'] / current_open) - 1) * 100
    current_bar['x1_ema9_real'] = data_5min[index-10]['ema9']
    current_bar['x1_ema21_real'] = data_5min[index-10]['ema21']
    current_bar['x1_ema55_real'] = data_5min[index-10]['ema55']
    current_bar['x1_ema144_real'] = data_5min[index-10]['ema144']
    current_bar['x1_ema233_real'] = data_5min[index-10]['ema233']
    current_bar['x1_open'] = (
        (data_5min[index-10]['open'] / current_open) - 1) * 100
    current_bar['x1_high'] = (
        (data_5min[index-10]['high'] / current_open) - 1) * 100
    current_bar['x1_low'] = (
        (data_5min[index-10]['low'] / current_open) - 1) * 100
    current_bar['x1_close'] = (
        (data_5min[index-10]['close'] / current_open) - 1) * 100
    current_bar['x1_volume'] = (
        (data_5min[index-10]['volume'] / current_volume) - 1) * 100
    current_bar['x1_open_real'] = data_5min[index-10]['open']
    current_bar['x1_high_real'] = data_5min[index-10]['high']
    current_bar['x1_low_real'] = data_5min[index-10]['low']
    current_bar['x1_close_real'] = data_5min[index-10]['close']
    current_bar['x1_height'] = current_bar['x1_high'] - current_bar['x1_low']
    current_bar['x1_body'] = ((max([current_bar['x1_open_real'],  current_bar['x1_close_real']]) /
                              min([current_bar['x1_open_real'],  current_bar['x1_close_real']])) - 1) * 100
    if current_bar['x1_open'] > current_bar['x1_close']:
        current_bar['x1_height'] *= -1
        current_bar['x1_body'] *= -1
    current_bar['x1_roc'] = (
        (current_bar['x1_open_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_ema9_close'] = (
        (current_bar['x1_ema9_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_ema21_close'] = (
        (current_bar['x1_ema21_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_ema55_close'] = (
        (current_bar['x1_ema55_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_ema144_close'] = (
        (current_bar['x1_ema144_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_ema233_close'] = (
        (current_bar['x1_ema233_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x1_x0_close'] = (
        (current_bar['x1_close_real'] / current_bar['x0_close_real']) - 1) * 100
    current_bar['x1_x0_high'] = (
        (current_bar['x1_high_real'] / current_bar['x0_high_real']) - 1) * 100
    current_bar['x1_x0_low'] = (
        (current_bar['x1_low_real'] / current_bar['x0_low_real']) - 1) * 100

    current_bar['x2_vwap'] = (
        (data_5min[index-9]['vwap'] / current_open) - 1) * 100
    current_bar['x2_ema9'] = (
        (data_5min[index-9]['ema9'] / current_open) - 1) * 100
    current_bar['x2_ema21'] = (
        (data_5min[index-9]['ema21'] / current_open) - 1) * 100
    current_bar['x2_ema55'] = (
        (data_5min[index-9]['ema55'] / current_open) - 1) * 100
    current_bar['x2_ema144'] = (
        (data_5min[index-9]['ema144'] / current_open) - 1) * 100
    current_bar['x2_ema233'] = (
        (data_5min[index-9]['ema233'] / current_open) - 1) * 100
    current_bar['x2_ema9_real'] = data_5min[index-9]['ema9']
    current_bar['x2_ema21_real'] = data_5min[index-9]['ema21']
    current_bar['x2_ema55_real'] = data_5min[index-9]['ema55']
    current_bar['x2_ema144_real'] = data_5min[index-9]['ema144']
    current_bar['x2_ema233_real'] = data_5min[index-9]['ema233']
    current_bar['x2_open'] = (
        (data_5min[index-9]['open'] / current_open) - 1) * 100
    current_bar['x2_high'] = (
        (data_5min[index-9]['high'] / current_open) - 1) * 100
    current_bar['x2_low'] = (
        (data_5min[index-9]['low'] / current_open) - 1) * 100
    current_bar['x2_close'] = (
        (data_5min[index-9]['close'] / current_open) - 1) * 100
    current_bar['x2_volume'] = (
        (data_5min[index-9]['volume'] / current_volume) - 1) * 100
    current_bar['x2_open_real'] = data_5min[index-9]['open']
    current_bar['x2_high_real'] = data_5min[index-9]['high']
    current_bar['x2_low_real'] = data_5min[index-9]['low']
    current_bar['x2_close_real'] = data_5min[index-9]['close']
    current_bar['x2_height'] = current_bar['x2_high'] - current_bar['x2_low']
    current_bar['x2_body'] = ((max([current_bar['x2_open_real'],  current_bar['x2_close_real']]) /
                              min([current_bar['x2_open_real'],  current_bar['x2_close_real']])) - 1) * 100
    if current_bar['x2_open'] > current_bar['x2_close']:
        current_bar['x2_height'] *= -1
        current_bar['x2_body'] *= -1
    current_bar['x2_roc'] = (
        (current_bar['x2_open_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_ema9_close'] = (
        (current_bar['x2_ema9_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_ema21_close'] = (
        (current_bar['x2_ema21_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_ema55_close'] = (
        (current_bar['x2_ema55_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_ema144_close'] = (
        (current_bar['x2_ema144_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_ema233_close'] = (
        (current_bar['x2_ema233_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x2_x1_close'] = (
        (current_bar['x2_close_real'] / current_bar['x1_close_real']) - 1) * 100
    current_bar['x2_x1_high'] = (
        (current_bar['x2_high_real'] / current_bar['x1_high_real']) - 1) * 100
    current_bar['x2_x1_low'] = (
        (current_bar['x2_low_real'] / current_bar['x1_low_real']) - 1) * 100

    current_bar['x3_vwap'] = (
        (data_5min[index-8]['vwap'] / current_open) - 1) * 100
    current_bar['x3_ema9'] = (
        (data_5min[index-8]['ema9'] / current_open) - 1) * 100
    current_bar['x3_ema21'] = (
        (data_5min[index-8]['ema21'] / current_open) - 1) * 100
    current_bar['x3_ema55'] = (
        (data_5min[index-8]['ema55'] / current_open) - 1) * 100
    current_bar['x3_ema144'] = (
        (data_5min[index-8]['ema144'] / current_open) - 1) * 100
    current_bar['x3_ema233'] = (
        (data_5min[index-8]['ema233'] / current_open) - 1) * 100
    current_bar['x3_ema9_real'] = data_5min[index-8]['ema9']
    current_bar['x3_ema21_real'] = data_5min[index-8]['ema21']
    current_bar['x3_ema55_real'] = data_5min[index-8]['ema55']
    current_bar['x3_ema144_real'] = data_5min[index-8]['ema144']
    current_bar['x3_ema233_real'] = data_5min[index-8]['ema233']
    current_bar['x3_open'] = (
        (data_5min[index-8]['open'] / current_open) - 1) * 100
    current_bar['x3_high'] = (
        (data_5min[index-8]['high'] / current_open) - 1) * 100
    current_bar['x3_low'] = (
        (data_5min[index-8]['low'] / current_open) - 1) * 100
    current_bar['x3_close'] = (
        (data_5min[index-8]['close'] / current_open) - 1) * 100
    current_bar['x3_volume'] = (
        (data_5min[index-8]['volume'] / current_volume) - 1) * 100
    current_bar['x3_open_real'] = data_5min[index-8]['open']
    current_bar['x3_high_real'] = data_5min[index-8]['high']
    current_bar['x3_low_real'] = data_5min[index-8]['low']
    current_bar['x3_close_real'] = data_5min[index-8]['close']
    current_bar['x3_height'] = current_bar['x3_high'] - current_bar['x3_low']
    current_bar['x3_body'] = ((max([current_bar['x3_open_real'],  current_bar['x3_close_real']]) /
                              min([current_bar['x3_open_real'],  current_bar['x3_close_real']])) - 1) * 100
    if current_bar['x3_open'] > current_bar['x3_close']:
        current_bar['x3_height'] *= -1
        current_bar['x3_body'] *= -1
    current_bar['x3_roc'] = (
        (current_bar['x3_open_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_ema9_close'] = (
        (current_bar['x3_ema9_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_ema21_close'] = (
        (current_bar['x3_ema21_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_ema55_close'] = (
        (current_bar['x3_ema55_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_ema144_close'] = (
        (current_bar['x3_ema144_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_ema233_close'] = (
        (current_bar['x3_ema233_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x3_x2_close'] = (
        (current_bar['x3_close_real'] / current_bar['x2_close_real']) - 1) * 100
    current_bar['x3_x2_high'] = (
        (current_bar['x3_high_real'] / current_bar['x2_high_real']) - 1) * 100
    current_bar['x3_x2_low'] = (
        (current_bar['x3_low_real'] / current_bar['x2_low_real']) - 1) * 100

    current_bar['x4_vwap'] = (
        (data_5min[index-7]['vwap'] / current_open) - 1) * 100
    current_bar['x4_ema9'] = (
        (data_5min[index-7]['ema9'] / current_open) - 1) * 100
    current_bar['x4_ema21'] = (
        (data_5min[index-7]['ema21'] / current_open) - 1) * 100
    current_bar['x4_ema55'] = (
        (data_5min[index-7]['ema55'] / current_open) - 1) * 100
    current_bar['x4_ema144'] = (
        (data_5min[index-7]['ema144'] / current_open) - 1) * 100
    current_bar['x4_ema233'] = (
        (data_5min[index-7]['ema233'] / current_open) - 1) * 100
    current_bar['x4_ema9_real'] = data_5min[index-7]['ema9']
    current_bar['x4_ema21_real'] = data_5min[index-7]['ema21']
    current_bar['x4_ema55_real'] = data_5min[index-7]['ema55']
    current_bar['x4_ema144_real'] = data_5min[index-7]['ema144']
    current_bar['x4_ema233_real'] = data_5min[index-7]['ema233']
    current_bar['x4_open'] = (
        (data_5min[index-7]['open'] / current_open) - 1) * 100
    current_bar['x4_high'] = (
        (data_5min[index-7]['high'] / current_open) - 1) * 100
    current_bar['x4_low'] = (
        (data_5min[index-7]['low'] / current_open) - 1) * 100
    current_bar['x4_close'] = (
        (data_5min[index-7]['close'] / current_open) - 1) * 100
    current_bar['x4_volume'] = (
        (data_5min[index-7]['volume'] / current_volume) - 1) * 100
    current_bar['x4_open_real'] = data_5min[index-7]['open']
    current_bar['x4_high_real'] = data_5min[index-7]['high']
    current_bar['x4_low_real'] = data_5min[index-7]['low']
    current_bar['x4_close_real'] = data_5min[index-7]['close']
    current_bar['x4_height'] = current_bar['x4_high'] - current_bar['x4_low']
    current_bar['x4_body'] = ((max([current_bar['x4_open_real'],  current_bar['x4_close_real']]) /
                              min([current_bar['x4_open_real'],  current_bar['x4_close_real']])) - 1) * 100
    if current_bar['x4_open'] > current_bar['x4_close']:
        current_bar['x4_height'] *= -1
        current_bar['x4_body'] *= -1
    current_bar['x4_roc'] = (
        (current_bar['x4_open_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_ema9_close'] = (
        (current_bar['x4_ema9_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_ema21_close'] = (
        (current_bar['x4_ema21_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_ema55_close'] = (
        (current_bar['x4_ema55_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_ema144_close'] = (
        (current_bar['x4_ema144_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_ema233_close'] = (
        (current_bar['x4_ema233_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x4_x3_close'] = (
        (current_bar['x4_close_real'] / current_bar['x3_close_real']) - 1) * 100
    current_bar['x4_x3_high'] = (
        (current_bar['x4_high_real'] / current_bar['x3_high_real']) - 1) * 100
    current_bar['x4_x3_low'] = (
        (current_bar['x4_low_real'] / current_bar['x3_low_real']) - 1) * 100

    current_bar['x5_vwap'] = (
        (data_5min[index-6]['vwap'] / current_open) - 1) * 100
    current_bar['x5_ema9'] = (
        (data_5min[index-6]['ema9'] / current_open) - 1) * 100
    current_bar['x5_ema21'] = (
        (data_5min[index-6]['ema21'] / current_open) - 1) * 100
    current_bar['x5_ema55'] = (
        (data_5min[index-6]['ema55'] / current_open) - 1) * 100
    current_bar['x5_ema144'] = (
        (data_5min[index-6]['ema144'] / current_open) - 1) * 100
    current_bar['x5_ema233'] = (
        (data_5min[index-6]['ema233'] / current_open) - 1) * 100
    current_bar['x5_ema9_real'] = data_5min[index-6]['ema9']
    current_bar['x5_ema21_real'] = data_5min[index-6]['ema21']
    current_bar['x5_ema55_real'] = data_5min[index-6]['ema55']
    current_bar['x5_ema144_real'] = data_5min[index-6]['ema144']
    current_bar['x5_ema233_real'] = data_5min[index-6]['ema233']
    current_bar['x5_open'] = (
        (data_5min[index-6]['open'] / current_open) - 1) * 100
    current_bar['x5_high'] = (
        (data_5min[index-6]['high'] / current_open) - 1) * 100
    current_bar['x5_low'] = (
        (data_5min[index-6]['low'] / current_open) - 1) * 100
    current_bar['x5_close'] = (
        (data_5min[index-6]['close'] / current_open) - 1) * 100
    current_bar['x5_volume'] = (
        (data_5min[index-6]['volume'] / current_volume) - 1) * 100
    current_bar['x5_open_real'] = data_5min[index-6]['open']
    current_bar['x5_high_real'] = data_5min[index-6]['high']
    current_bar['x5_low_real'] = data_5min[index-6]['low']
    current_bar['x5_close_real'] = data_5min[index-6]['close']
    current_bar['x5_height'] = current_bar['x5_high'] - current_bar['x5_low']
    current_bar['x5_body'] = ((max([current_bar['x5_open_real'],  current_bar['x5_close_real']]) /
                              min([current_bar['x5_open_real'],  current_bar['x5_close_real']])) - 1) * 100

    if current_bar['x5_open'] > current_bar['x5_close']:
        current_bar['x5_height'] *= -1
        current_bar['x5_body'] *= -1
    current_bar['x5_roc'] = (
        (current_bar['x5_open_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_ema9_close'] = (
        (current_bar['x5_ema9_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_ema21_close'] = (
        (current_bar['x5_ema21_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_ema55_close'] = (
        (current_bar['x5_ema55_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_ema144_close'] = (
        (current_bar['x5_ema144_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_ema233_close'] = (
        (current_bar['x5_ema233_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x5_x4_close'] = (
        (current_bar['x5_close_real'] / current_bar['x4_close_real']) - 1) * 100
    current_bar['x5_x4_high'] = (
        (current_bar['x5_high_real'] / current_bar['x4_high_real']) - 1) * 100
    current_bar['x5_x4_low'] = (
        (current_bar['x5_low_real'] / current_bar['x4_low_real']) - 1) * 100

    current_bar['x6_vwap'] = (
        (data_5min[index-5]['vwap'] / current_open) - 1) * 100
    current_bar['x6_ema9'] = (
        (data_5min[index-5]['ema9'] / current_open) - 1) * 100
    current_bar['x6_ema21'] = (
        (data_5min[index-5]['ema21'] / current_open) - 1) * 100
    current_bar['x6_ema55'] = (
        (data_5min[index-5]['ema55'] / current_open) - 1) * 100
    current_bar['x6_ema144'] = (
        (data_5min[index-5]['ema144'] / current_open) - 1) * 100
    current_bar['x6_ema233'] = (
        (data_5min[index-5]['ema233'] / current_open) - 1) * 100
    current_bar['x6_ema9_real'] = data_5min[index-5]['ema9']
    current_bar['x6_ema21_real'] = data_5min[index-5]['ema21']
    current_bar['x6_ema55_real'] = data_5min[index-5]['ema55']
    current_bar['x6_ema144_real'] = data_5min[index-5]['ema144']
    current_bar['x6_ema233_real'] = data_5min[index-5]['ema233']
    current_bar['x6_open'] = (
        (data_5min[index-5]['open'] / current_open) - 1) * 100
    current_bar['x6_high'] = (
        (data_5min[index-5]['high'] / current_open) - 1) * 100
    current_bar['x6_low'] = (
        (data_5min[index-5]['low'] / current_open) - 1) * 100
    current_bar['x6_close'] = (
        (data_5min[index-5]['close'] / current_open) - 1) * 100
    current_bar['x6_volume'] = (
        (data_5min[index-5]['volume'] / current_volume) - 1) * 100
    current_bar['x6_open_real'] = data_5min[index-5]['open']
    current_bar['x6_high_real'] = data_5min[index-5]['high']
    current_bar['x6_low_real'] = data_5min[index-5]['low']
    current_bar['x6_close_real'] = data_5min[index-5]['close']
    current_bar['x6_height'] = current_bar['x6_high'] - current_bar['x6_low']
    current_bar['x6_body'] = ((max([current_bar['x6_open_real'],  current_bar['x6_close_real']]) /
                              min([current_bar['x6_open_real'],  current_bar['x6_close_real']])) - 1) * 100
    if current_bar['x6_open'] > current_bar['x6_close']:
        current_bar['x6_height'] *= -1
        current_bar['x6_body'] *= -1
    current_bar['x6_roc'] = (
        (current_bar['x6_open_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_ema9_close'] = (
        (current_bar['x6_ema9_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_ema21_close'] = (
        (current_bar['x6_ema21_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_ema55_close'] = (
        (current_bar['x6_ema55_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_ema144_close'] = (
        (current_bar['x6_ema144_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_ema233_close'] = (
        (current_bar['x6_ema233_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x6_x5_close'] = (
        (current_bar['x6_close_real'] / current_bar['x5_close_real']) - 1) * 100
    current_bar['x6_x5_high'] = (
        (current_bar['x6_high_real'] / current_bar['x5_high_real']) - 1) * 100
    current_bar['x6_x5_low'] = (
        (current_bar['x6_low_real'] / current_bar['x5_low_real']) - 1) * 100

    current_bar['x7_vwap'] = (
        (data_5min[index-4]['vwap'] / current_open) - 1) * 100
    current_bar['x7_ema9'] = (
        (data_5min[index-4]['ema9'] / current_open) - 1) * 100
    current_bar['x7_ema21'] = (
        (data_5min[index-4]['ema21'] / current_open) - 1) * 100
    current_bar['x7_ema55'] = (
        (data_5min[index-4]['ema55'] / current_open) - 1) * 100
    current_bar['x7_ema144'] = (
        (data_5min[index-4]['ema144'] / current_open) - 1) * 100
    current_bar['x7_ema233'] = (
        (data_5min[index-4]['ema233'] / current_open) - 1) * 100
    current_bar['x7_ema9_real'] = data_5min[index-4]['ema9']
    current_bar['x7_ema21_real'] = data_5min[index-4]['ema21']
    current_bar['x7_ema55_real'] = data_5min[index-4]['ema55']
    current_bar['x7_ema144_real'] = data_5min[index-4]['ema144']
    current_bar['x7_ema233_real'] = data_5min[index-4]['ema233']
    current_bar['x7_open'] = (
        (data_5min[index-4]['open'] / current_open) - 1) * 100
    current_bar['x7_high'] = (
        (data_5min[index-4]['high'] / current_open) - 1) * 100
    current_bar['x7_low'] = (
        (data_5min[index-4]['low'] / current_open) - 1) * 100
    current_bar['x7_close'] = (
        (data_5min[index-4]['close'] / current_open) - 1) * 100
    current_bar['x7_volume'] = (
        (data_5min[index-4]['volume'] / current_volume) - 1) * 100
    current_bar['x7_open_real'] = data_5min[index-4]['open']
    current_bar['x7_high_real'] = data_5min[index-4]['high']
    current_bar['x7_low_real'] = data_5min[index-4]['low']
    current_bar['x7_close_real'] = data_5min[index-4]['close']
    current_bar['x7_height'] = current_bar['x7_high'] - current_bar['x7_low']
    current_bar['x7_body'] = ((max([current_bar['x7_open_real'],  current_bar['x7_close_real']]) /
                              min([current_bar['x7_open_real'],  current_bar['x7_close_real']])) - 1) * 100
    if current_bar['x7_open'] > current_bar['x7_close']:
        current_bar['x7_height'] *= -1
        current_bar['x7_body'] *= -1
    current_bar['x7_roc'] = (
        (current_bar['x7_open_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_ema9_close'] = (
        (current_bar['x7_ema9_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_ema21_close'] = (
        (current_bar['x7_ema21_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_ema55_close'] = (
        (current_bar['x7_ema55_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_ema144_close'] = (
        (current_bar['x7_ema144_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_ema233_close'] = (
        (current_bar['x7_ema233_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x7_x6_close'] = (
        (current_bar['x7_close_real'] / current_bar['x6_close_real']) - 1) * 100
    current_bar['x7_x6_high'] = (
        (current_bar['x7_high_real'] / current_bar['x6_high_real']) - 1) * 100
    current_bar['x7_x6_low'] = (
        (current_bar['x7_low_real'] / current_bar['x6_low_real']) - 1) * 100

    current_bar['x8_vwap'] = (
        (data_5min[index-3]['vwap'] / current_open) - 1) * 100
    current_bar['x8_ema9'] = (
        (data_5min[index-3]['ema9'] / current_open) - 1) * 100
    current_bar['x8_ema21'] = (
        (data_5min[index-3]['ema21'] / current_open) - 1) * 100
    current_bar['x8_ema55'] = (
        (data_5min[index-3]['ema55'] / current_open) - 1) * 100
    current_bar['x8_ema144'] = (
        (data_5min[index-3]['ema144'] / current_open) - 1) * 100
    current_bar['x8_ema233'] = (
        (data_5min[index-3]['ema233'] / current_open) - 1) * 100
    current_bar['x8_ema9_real'] = data_5min[index-3]['ema9']
    current_bar['x8_ema21_real'] = data_5min[index-3]['ema21']
    current_bar['x8_ema55_real'] = data_5min[index-3]['ema55']
    current_bar['x8_ema144_real'] = data_5min[index-3]['ema144']
    current_bar['x8_ema233_real'] = data_5min[index-3]['ema233']
    current_bar['x8_open'] = (
        (data_5min[index-3]['open'] / current_open) - 1) * 100
    current_bar['x8_high'] = (
        (data_5min[index-3]['high'] / current_open) - 1) * 100
    current_bar['x8_low'] = (
        (data_5min[index-3]['low'] / current_open) - 1) * 100
    current_bar['x8_close'] = (
        (data_5min[index-3]['close'] / current_open) - 1) * 100
    current_bar['x8_volume'] = (
        (data_5min[index-3]['volume'] / current_volume) - 1) * 100
    current_bar['x8_open_real'] = data_5min[index-3]['open']
    current_bar['x8_high_real'] = data_5min[index-3]['high']
    current_bar['x8_low_real'] = data_5min[index-3]['low']
    current_bar['x8_close_real'] = data_5min[index-3]['close']
    current_bar['x8_height'] = current_bar['x8_high'] - current_bar['x8_low']
    current_bar['x8_body'] = ((max([current_bar['x8_open_real'],  current_bar['x8_close_real']]) /
                              min([current_bar['x8_open_real'],  current_bar['x8_close_real']])) - 1) * 100
    if current_bar['x8_open'] > current_bar['x8_close']:
        current_bar['x8_height'] *= -1
        current_bar['x8_body'] *= -1
    current_bar['x8_roc'] = (
        (current_bar['x8_open_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_ema9_close'] = (
        (current_bar['x8_ema9_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_ema21_close'] = (
        (current_bar['x8_ema21_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_ema55_close'] = (
        (current_bar['x8_ema55_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_ema144_close'] = (
        (current_bar['x8_ema144_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_ema233_close'] = (
        (current_bar['x8_ema233_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x8_x7_close'] = (
        (current_bar['x8_close_real'] / current_bar['x7_close_real']) - 1) * 100
    current_bar['x8_x7_high'] = (
        (current_bar['x8_high_real'] / current_bar['x7_high_real']) - 1) * 100
    current_bar['x8_x7_low'] = (
        (current_bar['x8_low_real'] / current_bar['x7_low_real']) - 1) * 100

    current_bar['x9_vwap'] = (
        (data_5min[index-2]['vwap'] / current_open) - 1) * 100
    current_bar['x9_ema9'] = (
        (data_5min[index-2]['ema9'] / current_open) - 1) * 100
    current_bar['x9_ema21'] = (
        (data_5min[index-2]['ema21'] / current_open) - 1) * 100
    current_bar['x9_ema55'] = (
        (data_5min[index-2]['ema55'] / current_open) - 1) * 100
    current_bar['x9_ema144'] = (
        (data_5min[index-2]['ema144'] / current_open) - 1) * 100
    current_bar['x9_ema233'] = (
        (data_5min[index-2]['ema233'] / current_open) - 1) * 100
    current_bar['x9_ema9_real'] = data_5min[index-2]['ema9']
    current_bar['x9_ema21_real'] = data_5min[index-2]['ema21']
    current_bar['x9_ema55_real'] = data_5min[index-2]['ema55']
    current_bar['x9_ema144_real'] = data_5min[index-2]['ema144']
    current_bar['x9_ema233_real'] = data_5min[index-2]['ema233']
    current_bar['x9_open'] = (
        (data_5min[index-2]['open'] / current_open) - 1) * 100
    current_bar['x9_high'] = (
        (data_5min[index-2]['high'] / current_open) - 1) * 100
    current_bar['x9_low'] = (
        (data_5min[index-2]['low'] / current_open) - 1) * 100
    current_bar['x9_close'] = (
        (data_5min[index-2]['close'] / current_open) - 1) * 100
    current_bar['x9_volume'] = (
        (data_5min[index-2]['volume'] / current_volume) - 1) * 100
    current_bar['x9_open_real'] = data_5min[index-2]['open']
    current_bar['x9_high_real'] = data_5min[index-2]['high']
    current_bar['x9_low_real'] = data_5min[index-2]['low']
    current_bar['x9_close_real'] = data_5min[index-2]['close']
    current_bar['x9_height'] = current_bar['x9_high'] - current_bar['x9_low']
    current_bar['x9_body'] = ((max([current_bar['x9_open_real'],  current_bar['x9_close_real']]) /
                              min([current_bar['x9_open_real'],  current_bar['x9_close_real']])) - 1) * 100
    if current_bar['x9_open'] > current_bar['x9_close']:
        current_bar['x9_height'] *= -1
        current_bar['x9_body'] *= -1
    current_bar['x9_roc'] = (
        (current_bar['x9_open_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_ema9_close'] = (
        (current_bar['x9_ema9_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_ema21_close'] = (
        (current_bar['x9_ema21_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_ema55_close'] = (
        (current_bar['x9_ema55_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_ema144_close'] = (
        (current_bar['x9_ema144_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_ema233_close'] = (
        (current_bar['x9_ema233_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x9_x8_close'] = (
        (current_bar['x9_close_real'] / current_bar['x8_close_real']) - 1) * 100
    current_bar['x9_x8_high'] = (
        (current_bar['x9_high_real'] / current_bar['x8_high_real']) - 1) * 100
    current_bar['x9_x8_low'] = (
        (current_bar['x9_low_real'] / current_bar['x8_low_real']) - 1) * 100

    current_bar['x10_vwap'] = (
        (data_5min[index-1]['vwap'] / current_open) - 1) * 100
    current_bar['x10_ema9'] = (
        (data_5min[index-1]['ema9'] / current_open) - 1) * 100
    current_bar['x10_ema21'] = (
        (data_5min[index-1]['ema21'] / current_open) - 1) * 100
    current_bar['x10_ema55'] = (
        (data_5min[index-1]['ema55'] / current_open) - 1) * 100
    current_bar['x10_ema144'] = (
        (data_5min[index-1]['ema144'] / current_open) - 1) * 100
    current_bar['x10_ema233'] = (
        (data_5min[index-1]['ema233'] / current_open) - 1) * 100
    current_bar['x10_ema9_real'] = data_5min[index-1]['ema9']
    current_bar['x10_ema21_real'] = data_5min[index-1]['ema21']
    current_bar['x10_ema55_real'] = data_5min[index-1]['ema55']
    current_bar['x10_ema144_real'] = data_5min[index-1]['ema144']
    current_bar['x10_ema233_real'] = data_5min[index-1]['ema233']
    current_bar['x10_open'] = (
        (data_5min[index-1]['open'] / current_open) - 1) * 100
    current_bar['x10_high'] = (
        (data_5min[index-1]['high'] / current_open) - 1) * 100
    current_bar['x10_low'] = (
        (data_5min[index-1]['low'] / current_open) - 1) * 100
    current_bar['x10_close'] = (
        (data_5min[index-1]['close'] / current_open) - 1) * 100
    current_bar['x10_volume'] = (
        (data_5min[index-1]['volume'] / current_volume) - 1) * 100
    current_bar['x10_open_real'] = data_5min[index-1]['open']
    current_bar['x10_high_real'] = data_5min[index-1]['high']
    current_bar['x10_low_real'] = data_5min[index-1]['low']
    current_bar['x10_close_real'] = data_5min[index-1]['close']
    current_bar['x10_height'] = current_bar['x10_high'] - \
        current_bar['x10_low']
    current_bar['x10_body'] = ((max([current_bar['x10_open_real'],  current_bar['x10_close_real']]) /
                               min([current_bar['x10_open_real'],  current_bar['x10_close_real']])) - 1) * 100
    if current_bar['x10_open'] > current_bar['x10_close']:
        current_bar['x10_height'] *= -1
        current_bar['x10_body'] *= -1
    current_bar['x10_roc'] = (
        (current_bar['x10_open_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_ema9_close'] = (
        (current_bar['x10_ema9_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_ema21_close'] = (
        (current_bar['x10_ema21_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_ema55_close'] = (
        (current_bar['x10_ema55_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_ema144_close'] = (
        (current_bar['x10_ema144_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_ema233_close'] = (
        (current_bar['x10_ema233_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x10_x9_close'] = (
        (current_bar['x10_close_real'] / current_bar['x9_close_real']) - 1) * 100
    current_bar['x10_x9_high'] = (
        (current_bar['x10_high_real'] / current_bar['x9_high_real']) - 1) * 100
    current_bar['x10_x9_low'] = (
        (current_bar['x10_low_real'] / current_bar['x9_low_real']) - 1) * 100

    current_bar['x11_vwap'] = (
        (data_5min[index]['vwap'] / current_open) - 1) * 100
    current_bar['x11_ema9'] = (
        (data_5min[index]['ema9'] / current_open) - 1) * 100
    current_bar['x11_ema21'] = (
        (data_5min[index]['ema21'] / current_open) - 1) * 100
    current_bar['x11_ema55'] = (
        (data_5min[index]['ema55'] / current_open) - 1) * 100
    current_bar['x11_ema144'] = (
        (data_5min[index]['ema144'] / current_open) - 1) * 100
    current_bar['x11_ema233'] = (
        (data_5min[index]['ema233'] / current_open) - 1) * 100
    current_bar['x11_ema9_real'] = data_5min[index]['ema9']
    current_bar['x11_ema21_real'] = data_5min[index]['ema21']
    current_bar['x11_ema55_real'] = data_5min[index]['ema55']
    current_bar['x11_ema144_real'] = data_5min[index]['ema144']
    current_bar['x11_ema233_real'] = data_5min[index]['ema233']
    current_bar['x11_open'] = (
        (data_5min[index]['open'] / current_open) - 1) * 100
    current_bar['x11_high'] = (
        (data_5min[index]['high'] / current_open) - 1) * 100
    current_bar['x11_low'] = (
        (data_5min[index]['low'] / current_open) - 1) * 100
    current_bar['x11_close'] = (
        (data_5min[index]['close'] / current_open) - 1) * 100
    current_bar['x11_volume'] = (
        (data_5min[index]['volume'] / current_volume) - 1) * 100
    current_bar['x11_open_real'] = data_5min[index]['open']
    current_bar['x11_high_real'] = data_5min[index]['high']
    current_bar['x11_low_real'] = data_5min[index]['low']
    current_bar['x11_close_real'] = data_5min[index]['close']
    current_bar['x11_height'] = current_bar['x11_high'] - \
        current_bar['x11_low']
    current_bar['x11_body'] = ((max([current_bar['x11_open_real'],  current_bar['x11_close_real']]) /
                               min([current_bar['x11_open_real'],  current_bar['x11_close_real']])) - 1) * 100
    if current_bar['x11_open'] > current_bar['x11_close']:
        current_bar['x11_height'] *= -1
        current_bar['x11_body'] *= -1
    current_bar['x11_roc'] = (
        (current_bar['x11_open_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_previous_high'] = (
        (current_bar['previous_high_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_previous_low'] = (
        (current_bar['previous_low_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_previous_close'] = (
        (current_bar['previous_close_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_previous_open'] = (
        (current_bar['previous_open_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_ema9_close'] = (
        (current_bar['x11_ema9_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_ema21_close'] = (
        (current_bar['x11_ema21_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_ema55_close'] = (
        (current_bar['x11_ema55_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_ema144_close'] = (
        (current_bar['x11_ema144_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_ema233_close'] = (
        (current_bar['x11_ema233_real'] / current_bar['x11_close_real']) - 1) * 100
    current_bar['x11_x10_close'] = (
        (current_bar['x11_close_real'] / current_bar['x10_close_real']) - 1) * 100
    current_bar['x11_x10_high'] = (
        (current_bar['x11_high_real'] / current_bar['x10_high_real']) - 1) * 100
    current_bar['x11_x10_low'] = (
        (current_bar['x11_low_real'] / current_bar['x10_low_real']) - 1) * 100

    current_bar['x11_high_slope'] = get_slope(current_bar, 'high')
    current_bar['x11_low_slope'] = get_slope(current_bar, 'low')
    current_bar['x11_close_slope'] = get_slope(current_bar, 'low')
    current_bar['x11_volume_slope'] = get_slope(current_bar, 'volume')

    current_bar['current_pos'] = current_bar['x11_close']
    current_bar['current_date'] = current_date

    generated_bars.append(current_bar)

    if model_to_use is None:
        model_to_use = return_first_model(DATA_OUTPUT_DIR)
        best_short_booster = joblib.load(model_to_use['xgboostshortmodel'])
        best_long_booster = joblib.load(model_to_use['xgboostlongmodel'])

    df_current_total_dataset = calculate_predict(generated_bars, parameters)

    ret_dict = df_current_total_dataset.to_dict('records')

    if DATA_OUTPUT_DIR is not None and False:
        test_predict = os.path.join(DATA_OUTPUT_DIR, 'saida_test_predict.xlsx')
        df_current_total_dataset.to_excel(test_predict)

    predict = {
        'short_predict': ret_dict[0]['short_predict'],
        'long_predict': ret_dict[0]['long_predict']}

    predict_cache[predict_key] = predict
    return predict
