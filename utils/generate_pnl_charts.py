import os
import sys
import time
import glob
import shutil
import pandas as pd
import matplotlib
import matplotlib.pyplot


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
        python('Strategies folder was not found...')
        sys.exit(-1)
    if not os.path.exists(PYAUTOTRADER_STRATEGIES_SUMMARY):
        python('Strategies Summary was not found...')
        sys.exit(-1)

    return {
        "PYAUTOTRADER_STRATEGIES_FOLDER": PYAUTOTRADER_STRATEGIES_FOLDER,
        "PYAUTOTRADER_STRATEGIES_SUMMARY": PYAUTOTRADER_STRATEGIES_SUMMARY
    }


def generate_pnl_charts(PYAUTOTRADER_STRATEGIES_FOLDER, PYAUTOTRADER_STRATEGIES_SUMMARY):
    dfStrategies = pd.read_excel(PYAUTOTRADER_STRATEGIES_SUMMARY)
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
        for current_trade in test_trades_path:
            sum += current_trade['result']
            trades.append(
                {'DateTime': str(current_trade['Date']), 'Total': sum})

        dfPNL = pd.DataFrame(trades)
        PNL_CURRENT_FILE = os.path.join(
            PNL_FOLDER, current_strategy['pnl_chart_image'])

        figure = dfPNL.plot.line(
            x='DateTime', y='Total', figsize=(24, 12)).get_figure()
        figure.savefig(PNL_CURRENT_FILE)
        # figure.close()
        matplotlib.pyplot.close(figure)

        PNL_SAVE_FILE = os.path.join(PYAUTOTRADER_STRATEGIES_FOLDER, str(
            current_strategy['current_strategy']), current_strategy['pnl_chart_image'])
        shutil.copy(PNL_CURRENT_FILE, PNL_SAVE_FILE)


if __name__ == '__main__':
    ret = sanity_check()
    PYAUTOTRADER_STRATEGIES_FOLDER = ret["PYAUTOTRADER_STRATEGIES_FOLDER"]
    PYAUTOTRADER_STRATEGIES_SUMMARY = ret["PYAUTOTRADER_STRATEGIES_SUMMARY"]

    generate_pnl_charts(PYAUTOTRADER_STRATEGIES_FOLDER,
                        PYAUTOTRADER_STRATEGIES_SUMMARY)
