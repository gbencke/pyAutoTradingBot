import os
from datetime import datetime, timedelta
import pandas as pd


def get_minimal_datetime(data):
    datetimes = list(
        set([x['datetime'].split(' ')[0].replace('.', '-') for x in data]))

    datetimes.sort()
    final_datetime = datetimes[0] + ' 09:00'

    return datetime.strptime(final_datetime, "%Y-%m-%d %H:%M")


def get_last_date_time(data):
    datetimes = list(
        set([x['datetime'].split(' ')[0].replace('.', '-') for x in data]))

    datetimes.sort()
    final_datetime = datetimes[-1] + ' 09:00'

    return datetime.strptime(final_datetime, "%Y-%m-%d %H:%M") + timedelta(days=1)


def generate_candle(candle_data, data, current_date_time, aggregation):
    generated_candles = []
    for x in range(aggregation):
        candle_date_time = datetime.strftime(
            current_date_time + timedelta(minutes=x * 5), "%Y.%m.%d %H:%M")
        if candle_date_time in candle_data:
            generated_candles.append(candle_data[candle_date_time])

    if len(generated_candles) == (aggregation):
        return {
            'datetime': generated_candles[0]['datetime'],
            'open': generated_candles[0]['open'],
            'high': max([x['high'] for x in generated_candles]),
            'low': min([x['low'] for x in generated_candles]),
            'close': generated_candles[aggregation-1]['close'],
            'business': sum([x['business'] for x in generated_candles]),
            'volume': sum([x['volume'] for x in generated_candles])
        }


def aggregate_data_from_csv(args):
    if args.source is None:
        print("Missing --source parameter")
        sys.exit(1)
    if args.destination is None:
        print("Missing --destination parameter")
        sys.exit(1)
    if args.timeframe is None:
        print("Missing --timeframe parameter")
        sys.exit(1)

    if args.timeframe not in ['5Min', '15Min', '10Min']:
        print("Timeframe should be in 5Min, 15Min, 10Min")
        sys.exit(1)

    aggregation = int(int(args.timeframe.replace('Min', '')) / 5)
    data = pd.read_csv(args.source).to_dict('records')
    current_date_time = get_minimal_datetime(data)
    last_date_time = get_last_date_time(data)
    candle_data = {x['datetime']: x for x in data}

    candles = []

    while(last_date_time != current_date_time):
        current_candle = generate_candle(
            candle_data, data, current_date_time, aggregation)
        if current_candle is not None:
            candles.append(current_candle)
        current_date_time = current_date_time + \
            timedelta(minutes=aggregation * 5)

    linhas_saida = []
    linhas_saida.append('datetime,open,high,low,close,business,volume')
    linhas_saida += [f"{x['datetime']},{x['open']},{x['high']},{x['low']},{x['close']},{x['business']},{x['volume']}" for x in candles]

    with open(args.destination, 'w') as f:
        f.writelines([x+'\n' for x in linhas_saida])
