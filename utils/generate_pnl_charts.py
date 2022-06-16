import os
import sys
import time
import glob
import shutil
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot
from scipy import stats


def sanity_check():
    if 'PYAUTOTRADER_ROOT' not in os.environ:
        print("You need to specify the PYAUTOTRADER_ROOT environment variable to run the script...")
        sys.exit(-1)
    else:
        PYAUTOTRADER_ROOT = os.environ['PYAUTOTRADER_ROOT']

    PYAUTOTRADER_STRATEGIES_FOLDER = os.path.join(
        PYAUTOTRADER_ROOT, 'src', 'strategies', 'B3', 'WDOL', '00.data', 'strategies')

    PYAUTOTRADER_STRATEGIES_SUMMARY = os.path.join(
        PYAUTOTRADER_ROOT, 'src', 'strategies', 'B3', 'WDOL', '00.data', 'strategies', 'strategy_summary.xlsx')

    if not os.path.exists(PYAUTOTRADER_STRATEGIES_FOLDER):
        print('Strategies folder was not found...')
        sys.exit(-1)
    if not os.path.exists(PYAUTOTRADER_STRATEGIES_SUMMARY):
        print('Strategies Summary was not found...')
        sys.exit(-1)

    return {
        "PYAUTOTRADER_STRATEGIES_FOLDER": PYAUTOTRADER_STRATEGIES_FOLDER,
        "PYAUTOTRADER_STRATEGIES_SUMMARY": PYAUTOTRADER_STRATEGIES_SUMMARY
    }


def generate_pnl_charts(PYAUTOTRADER_STRATEGIES_FOLDER, PYAUTOTRADER_STRATEGIES_SUMMARY):
    dfStrategies = pd.read_excel(PYAUTOTRADER_STRATEGIES_SUMMARY, converters={
                                 'current_strategy': str})
    strategies = dfStrategies.to_dict('records')

    PNL_FOLDER = os.path.join(PYAUTOTRADER_STRATEGIES_FOLDER, 'pnl_charts')

    if not os.path.exists(PNL_FOLDER):
        os.mkdir(PNL_FOLDER)

    strategies = [
        {**x,
            'pnl_chart_image': f'{int(x["total_result"]):06d}.{x["current_strategy"]}.png'}
        for x in strategies]

    matplotlib.use('Agg')
    matplotlib.pyplot.ioff()

    linregs = []

    for current_strategy in strategies:
        if current_strategy['total_result'] < 0:
            continue
        test_trades_path = ''
        SEARCH_PATH = os.path.join(PYAUTOTRADER_STRATEGIES_FOLDER, str(
            current_strategy['current_strategy']), '*.test_trades.xlsx')
        for current_trades_files in glob.glob(SEARCH_PATH):
            test_trades_path = current_trades_files

        if test_trades_path == '':
            print(
                f'Could not find test_trades for {current_strategy["current_strategy"]}')
            continue

        dfTestTrades = pd.read_excel(test_trades_path)
        test_trades_path = dfTestTrades.to_dict('records')

        sum = 0
        trades = []
        counter = 0
        for current_trade in test_trades_path:
            if np.isnan(current_trade['result']):
                sum += 0
            else:
                sum += current_trade['result']
            trades.append(
                {'Counter': counter, 'DateTime': str(current_trade['Date']), 'Total': sum})
            counter += 1

        dfPNL = pd.DataFrame(trades)
        PNL_CURRENT_FILE = os.path.join(
            PNL_FOLDER, current_strategy['pnl_chart_image'])

        figure = dfPNL.plot.line(
            x='DateTime', y='Total', figsize=(12, 6)).get_figure()
        figure.savefig(PNL_CURRENT_FILE)
        matplotlib.pyplot.close(figure)

        PNL_SAVE_FILE = os.path.join(PYAUTOTRADER_STRATEGIES_FOLDER, str(
            current_strategy['current_strategy']), current_strategy['pnl_chart_image'])
        shutil.copy(PNL_CURRENT_FILE, PNL_SAVE_FILE)

        x = [x['Total'] for x in trades]
        y = [x['Counter'] for x in trades]
        slope, intercept, r, p, std_err = stats.linregress(x, y)
        linregs.append(
            {
                'strategy': current_strategy['current_strategy'],
                'total_result': current_strategy['total_result'],
                'percent_of_winning': current_strategy['percent_of_winning'],
                'avg_result': current_strategy['avg_result'],
                'slope': slope,
                'intercept': intercept,
                'r': r,
                'p': p,
                'std_err': std_err
            }
        )
    return linregs


if __name__ == '__main__':
    ret = sanity_check()
    PYAUTOTRADER_STRATEGIES_FOLDER = ret["PYAUTOTRADER_STRATEGIES_FOLDER"]
    PYAUTOTRADER_STRATEGIES_SUMMARY = ret["PYAUTOTRADER_STRATEGIES_SUMMARY"]

    linregs = generate_pnl_charts(PYAUTOTRADER_STRATEGIES_FOLDER,
                                  PYAUTOTRADER_STRATEGIES_SUMMARY)

    pnl_summary_file = os.path.join(
        PYAUTOTRADER_STRATEGIES_FOLDER, 'pnl_summary.xlsx')
    pnl_df = pd.DataFrame(linregs)
    pnl_df.to_excel(pnl_summary_file)
