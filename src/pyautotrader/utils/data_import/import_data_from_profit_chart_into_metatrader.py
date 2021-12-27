import sys
import os
import datetime
import pandas as pd

SOURCE_CSV_5MIN = ['asset', 'date', 'time', 'open',
                   'high', 'low', 'close', 'business', 'volume']
SOURCE_CSV_DAILY = ['asset', 'date', 'open', 'high',
                    'low', 'close', 'business', 'volume']


def format_value(x):
    return str(x).replace(',', '.')


def format_int_value(x):
    return str(int(float(str(x).replace(',', "."))))


def format_datetime(date, time):
    if time is not None:
        a = str(date) + ' '+str(time)
        return datetime.datetime.strptime(
            a, '%d/%m/%Y %H:%M:%S').strftime('%Y.%m.%d %H:%M')
    else:
        a = str(date)
        return datetime.datetime.strptime(a, '%d/%m/%Y').strftime('%Y.%m.%d')


def read_source_records(source):
    csv = pd.read_csv(source, delimiter=';')
    csv_read = csv.to_dict('records')
    if list(csv_read[0].keys()) == SOURCE_CSV_DAILY:
        periodicity = 'DAILY'
    elif list(csv_read[0].keys()) == SOURCE_CSV_5MIN:
        periodicity = '5MIN'
    else:
        print('CSV File doesn\'t have correct field headers')
        sys.exit(0)
    return periodicity, csv_read


def import_data_from_profit_chart_into_metatrader(source, destination, initialdate):
    if not os.path.exists(source):
        print(f'{source} file does not exist...')
    periodicity, source_records = read_source_records(source)
    if os.path.exists(destination):
        print('f{destination} file exists, appending')
    else:
        destination_records = [{
            'datetime': format_datetime(x['date'], x['time'] if periodicity != 'DAILY' else None),
            'open': format_value(x['open']),
            'high': format_value(x['high']),
            'low': format_value(x['low']),
            'close': format_value(x['close']),
            'business': format_int_value(x['business']),
            'volume': format_int_value(x['volume'])
        } for x in source_records]
        destination_records = sorted(
            destination_records, key=lambda x: x['datetime'])
        if initialdate is not None and False:
            destination_records = [
                x for x in destination_records if x['datetime'] >= initialdate]
        df_to_csv = pd.DataFrame(destination_records)
        df_to_csv.to_csv(destination, index=False)
        print('Generated:' + destination.split('\\')[-1])
