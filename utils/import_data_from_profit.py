import sys
import datetime
import os
import glob
import subprocess
import pandas as pd

PYAUTOTRADER_PROFITCHART_CSV_FOLDER = None
PYAUTOTRADER_ROOT = None
PYAUTOTRADER_CSV_INPUT_SEARCH = None
PYAUTOTRADER_CSV_INPUT = None


def sanity_check():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    if 'PYAUTOTRADER_PROFITCHART_CSV_FOLDER' not in os.environ:
        print("You need to specify the PYAUTOTRADER_PROFITCHART_CSV_FOLDER environment variable to run the script...")
        sys.exit(-1)
    else:
        PYAUTOTRADER_PROFITCHART_CSV_FOLDER = os.environ['PYAUTOTRADER_PROFITCHART_CSV_FOLDER']

    if 'PYAUTOTRADER_ROOT' not in os.environ:
        print("You need to specify the PYAUTOTRADER_ROOT environment variable to run the script...")
        sys.exit(-1)
    else:
        PYAUTOTRADER_ROOT = os.environ['PYAUTOTRADER_ROOT']

    if not os.path.exists(os.path.join(PYAUTOTRADER_PROFITCHART_CSV_FOLDER, 'WDOFUT_F_0_Diário.csv')):
        print("Could not find the Diario file in the ProfitChart CSV files to import...")
        sys.exit(-1)

    if not os.path.exists(os.path.join(PYAUTOTRADER_PROFITCHART_CSV_FOLDER, 'WDOFUT_F_0_5Min.csv')):
        print("Could not find the 5min file in the ProfitChart CSV files to import...")
        sys.exit(-1)

    PYAUTOTRADER_CSV_INPUT = os.path.join(
        PYAUTOTRADER_ROOT, 'src', 'strategies', 'B3', 'WDOL', '00.data', 'input')
    PYAUTOTRADER_CSV_INPUT_SEARCH = os.path.join(
        PYAUTOTRADER_ROOT, 'src', 'strategies', 'B3', 'WDOL', '00.data', 'input', '*.csv')


def rename_old_files():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    for current_csv_file in glob.glob(PYAUTOTRADER_CSV_INPUT_SEARCH):
        if current_csv_file.endswith('.old.csv'):

            continue
        os.rename(current_csv_file, current_csv_file.replace('.csv', '.old.csv'))


def check_if_old_files_exist():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    if not os.path.exists(os.path.join(PYAUTOTRADER_CSV_INPUT, 'WDO$Daily.old.csv')):
        print("Could not find the Daily quotes old file in the ProfitChart CSV files to import...")
        sys.exit(-1)

    if not os.path.exists(os.path.join(PYAUTOTRADER_CSV_INPUT, 'WDO$M5.old.csv')):
        print("Could not find the 5min quotes old file in the ProfitChart CSV files to import...")
        sys.exit(-1)


def process_daily_files():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    pdDailyNewEntries = pd.read_csv(os.path.join(
        PYAUTOTRADER_PROFITCHART_CSV_FOLDER, 'WDOFUT_F_0_Diário.csv'),
        sep=';',
        header=None,
        names=['asset', 'date', 'open', 'high', 'low', 'close', 'business', 'volume'])
    DailyNewEntries = pdDailyNewEntries.to_dict('records')
    DailyNewEntries = [{
        'datetime': datetime.datetime.strptime(x['date'], '%d/%m/%Y').strftime('%Y.%m.%d'),
        'open': float(x['open'].replace(',', '.')),
        'high': float(x['high'].replace(',', '.')),
        'low': float(x['low'].replace(',', '.')),
        'close': float(x['close'].replace(',', '.')),
        'business': int(float(x['business'].replace(',', '.'))),
        'volume': x['volume']
    } for x in DailyNewEntries]

    DailyNewEntriesIndex = {x['datetime']: x for x in DailyNewEntries}
    DailyNewEntriesList = [x['datetime'] for x in DailyNewEntries]
    DailyNewEntriesList.sort()

    pdDailyOldEntries = pd.read_csv(os.path.join(
        PYAUTOTRADER_CSV_INPUT, 'WDO$Daily.old.csv'))
    DailyOldEntries = pdDailyOldEntries.to_dict('records')
    DailyOldEntriesIndex = {x['datetime']: x for x in DailyOldEntries}
    DailyOldEntriesList = [x['datetime'] for x in DailyOldEntries]

    for current_entry in DailyNewEntriesList:
        if not current_entry in DailyOldEntriesIndex:
            DailyOldEntries.append(DailyNewEntriesIndex[current_entry])

    UpdatedOldEntries = pd.DataFrame(DailyOldEntries)
    UpdatedOldEntries.to_csv(os.path.join(
        PYAUTOTRADER_CSV_INPUT, 'WDO$Daily.csv'), index=False)


def process_5Min_files():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    pdM5NewEntries = pd.read_csv(os.path.join(
        PYAUTOTRADER_PROFITCHART_CSV_FOLDER, 'WDOFUT_F_0_5min.csv'),
        sep=';',
        header=None,
        names=['asset', 'date', 'time', 'open', 'high', 'low', 'close', 'business', 'volume'])
    M5NewEntries = pdM5NewEntries.to_dict('records')
    M5NewEntries = [{
        'datetime': datetime.datetime.strptime(x['date'] + ' ' + x['time'], '%d/%m/%Y %H:%M:%S').strftime('%Y.%m.%d %H:%M'),
        'open': float(x['open'].replace(',', '.')),
        'high': float(x['high'].replace(',', '.')),
        'low': float(x['low'].replace(',', '.')),
        'close': float(x['close'].replace(',', '.')),
        'business': int(float(x['business'].replace(',', '.'))),
        'volume': x['volume']
    } for x in M5NewEntries]

    M5NewEntriesIndex = {x['datetime']: x for x in M5NewEntries}
    M5NewEntriesList = [x['datetime'] for x in M5NewEntries]
    M5NewEntriesList.sort()

    pdM5OldEntries = pd.read_csv(os.path.join(
        PYAUTOTRADER_CSV_INPUT, 'WDO$M5.old.csv'))
    M5OldEntries = pdM5OldEntries.to_dict('records')
    M5OldEntriesIndex = {x['datetime']: x for x in M5OldEntries}
    M5OldEntriesList = [x['datetime'] for x in M5OldEntries]

    for current_entry in M5NewEntriesList:
        if not current_entry in M5OldEntriesIndex:
            M5OldEntries.append(M5NewEntriesIndex[current_entry])

    UpdatedOldEntries = pd.DataFrame(M5OldEntries)
    UpdatedOldEntries.to_csv(os.path.join(
        PYAUTOTRADER_CSV_INPUT, 'WDO$M5.csv'), index=False)


def remove_old_files():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    for current_csv_file in glob.glob(os.path.join(PYAUTOTRADER_CSV_INPUT, "*.old.csv")):
        os.unlink(current_csv_file)


def aggregate_files():
    global PYAUTOTRADER_PROFITCHART_CSV_FOLDER
    global PYAUTOTRADER_ROOT
    global PYAUTOTRADER_CSV_INPUT_SEARCH
    global PYAUTOTRADER_CSV_INPUT

    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.join(PYAUTOTRADER_ROOT, "src")
    env['VIRTUAL_ENV'] = "C:\\git\\216\\env"
    os.chdir(os.path.join(PYAUTOTRADER_ROOT, "src", "pyautotrader"))

    args = ["python.exe",
            "__main__.py",
            "aggregate_data_from_csv",
            "--source",
            os.path.join(PYAUTOTRADER_CSV_INPUT, "WDO$M5.csv"),
            "--destination",
            os.path.join(PYAUTOTRADER_CSV_INPUT, "WDO$M15.csv"),
            "--timeframe",
            "15Min"]

    print(subprocess.run(args, env=env))

    args = ["python.exe",
            "__main__.py",
            "aggregate_data_from_csv",
            "--source",
            os.path.join(PYAUTOTRADER_CSV_INPUT, "WDO$M5.csv"),
            "--destination",
            os.path.join(PYAUTOTRADER_CSV_INPUT, "WDO$M10.csv"),
            "--timeframe",
            "10Min"]

    print(subprocess.run(args, env=env))


if __name__ == '__main__':
    sanity_check()
    rename_old_files()
    rename_old_files()
    process_daily_files()
    process_5Min_files()
    remove_old_files()
    aggregate_files()
