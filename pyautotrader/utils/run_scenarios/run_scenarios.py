import glob
import time
import os
import sys
import papermill as pm
import pandas as pd
import joblib
import shutil
from datetime import datetime
from ilock import ILock


def get_short_score(current_strategy_folder):
    for current_file in glob.glob(os.path.join(current_strategy_folder, "*.short.train.score.txt")):
        with open(current_file, "r") as f:
            ret = f.read()
            return float(ret)
    return 0


def get_long_score(current_strategy_folder):
    for current_file in glob.glob(os.path.join(current_strategy_folder, "*.long.train.score.txt")):
        with open(current_file, "r") as f:
            ret = f.read()
            return float(ret)
    return 0


def summarize_scenarios(args):
    summarize()


def summarize():
    strategies_run = []

    current_strategies_folder = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'strategies')

    final_excel_summary = os.path.join(
        current_strategies_folder, 'strategy_summary.xlsx')

    strategies = set([x[0].replace(current_strategies_folder, '').split(os.sep)[1]
                      for x in os.walk(current_strategies_folder)
                      if x[0] != current_strategies_folder])

    for current_strategy in strategies:
        print("Processing:" + current_strategy)
        current_strategy_folder = os.path.join(
            current_strategies_folder, current_strategy)

        parameter_file = [x for x in os.listdir(
            current_strategy_folder) if x.endswith('parameters.pickle')]
        if len(parameter_file) == 0:
            continue
        else:
            parameter_file = os.path.join(
                current_strategy_folder, parameter_file[0])
        current_parameters = joblib.load(parameter_file)

        # -----------------------------

        test_trades = [x for x in os.listdir(
            current_strategy_folder) if x.endswith('test_trades.xlsx')]
        if len(test_trades) == 0:
            continue
        else:
            test_trades = os.path.join(current_strategy_folder, test_trades[0])

        trades = pd.read_excel(test_trades)

        # --------------------------------

        predicts = [x for x in os.listdir(
            current_strategy_folder) if x.endswith('predicts.xlsx')]
        if len(predicts) == 0:
            continue
        else:
            predicts = os.path.join(current_strategy_folder, predicts[0])

        predicts = pd.read_excel(predicts)

        # --------------------------------

        check_train = [x for x in os.listdir(
            current_strategy_folder) if x.endswith('check_model.xlsx')]
        if len(check_train) == 0:
            continue
        else:
            check_train = os.path.join(current_strategy_folder, check_train[0])

        check_train = pd.read_excel(check_train)

        # --------------------------------

        if len(trades.index) == 0 or (not 'result' in trades):
            continue

        def short_cost(df_short):
            valid_rows = 0
            error_row = 0

            for _, row in df_short.iterrows():
                row_is_short = 1 if row['is_short'] > 0 else 0
                row_is_short_predict = 1 if row['short_predict'] >= current_parameters['DECISION_BOUNDARY'] else 0
                if not (row_is_short == 0 and row_is_short_predict == 0):
                    valid_rows += 1
                else:
                    continue
                if row_is_short != row_is_short_predict:
                    error_row += 1

            return error_row / valid_rows

        def long_cost(df_long):
            valid_rows = 0
            error_row = 0

            for _, row in df_long.iterrows():
                row_is_long = 1 if row['is_long'] > 0 else 0
                row_is_long_predict = 1 if row['long_predict'] >= current_parameters['DECISION_BOUNDARY'] else 0
                if not (row_is_long == 0 and row_is_long_predict == 0):
                    valid_rows += 1
                else:
                    continue
                if row_is_long != row_is_long_predict:
                    error_row += 1

            return error_row / valid_rows

        print("Will add " + current_strategy)

        strategies_run.append({
            "current_strategy": current_strategy,
            "current_exchange": current_parameters['CURRENT_EXCHANGE'],
            "minimum_time": current_parameters['MINIMUM_TIME'],
            "maximum_time": current_parameters['MAXIMUM_TIME'],
            "minimum_date_dataframe": current_parameters['MINIMUM_DATE_DATAFRAME'],
            "minimum_date_trade": current_parameters['MINIMUM_DATE_TRADE'],
            "max_train_date": current_parameters['MAX_TRAIN_DATE'],
            "max_trade_duration": current_parameters['MAX_TRADE_DURATION'],
            "num_trees": current_parameters['NUM_TREES'],
            "tree_depth": current_parameters['TREE_DEPTH'],
            "weight_ratio": current_parameters['WEIGHT_RATIO'],
            "current_target": current_parameters['CURRENT_TARGET'],
            "current_stop": current_parameters['CURRENT_STOP'],
            "current_asset": current_parameters['CURRENT_ASSET'],
            "current_timeframe": current_parameters['CURRENT_TIMEFRAME'],
            "decision_boundary": current_parameters['DECISION_BOUNDARY'],
            "total_result": trades['result'].sum(),
            "avg_result": trades['result'].mean(),
            "number_of_trades": int(trades['result'].count()),
            'number_of_positive_trades': trades[trades['result'] >= 0].shape[0],
            'number_of_negative_trades': trades[trades['result'] < 0].shape[0],
            'percent_of_winning':  (trades[trades['result'] >= 0].shape[0] / trades['result'].count()) * 100,
            'max_winner': trades['result'].max(),
            'max_loser': trades['result'].min(),
            'first_trade': str(trades['Date'].min()),
            'last_trade': str(trades['Date'].max()),
            'test_short_cost': short_cost(predicts),
            'test_long_cost': long_cost(predicts),
            'train_short_cost': short_cost(check_train),
            'train_long_cost': long_cost(check_train),
            'train_short_score': get_short_score(current_strategy_folder),
            'train_long_score': get_long_score(current_strategy_folder),
        })

    pd.DataFrame(strategies_run).to_excel(final_excel_summary)


def run_notebook():
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")+"."+str(os.getpid())

    current_folder = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '02.candle_strategy')
    current_strategies = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'strategies')
    current_cache = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'strategies', 'cache')

    os.mkdir(os.path.join(current_strategies, current_date))
    current_strategies = os.path.join(current_strategies, current_date)

    os.environ["DATA_OUTPUT_DIR"] = current_strategies

    with ILock('Create Cache', timeout=1500000):
        if not os.path.exists(current_cache):
            input_notebook = os.path.join(
                current_folder, '02.candle_strategy_0100_create_dataframe.ipynb')
            output_notebook = os.path.join(
                current_strategies, '02.candle_strategy_0100_create_dataframe.executed.ipynb')

            pm.execute_notebook(input_notebook, output_notebook)

            if not os.path.exists(current_cache):
                os.mkdir(current_cache)

            for f in os.listdir(current_cache):
                os.remove(os.path.join(current_cache, f))

            for f in os.listdir(current_strategies):
                shutil.copyfile(os.path.join(current_strategies, f),
                                os.path.join(current_cache, f))

        else:
            for f in os.listdir(current_cache):
                shutil.copyfile(os.path.join(current_cache, f),
                                os.path.join(current_strategies, f))

    input_notebook = os.path.join(
        current_folder, '02.candle_strategy_0200_create_xgbooster.ipynb')
    output_notebook = os.path.join(
        current_strategies, '02.candle_strategy_0200_create_xgbooster.executed.ipynb')

    pm.execute_notebook(input_notebook, output_notebook)

    input_notebook = os.path.join(
        current_folder, '02.candle_strategy_0300_find_decision_boundary.ipynb')
    output_notebook = os.path.join(
        current_strategies, '02.candle_strategy_0300_find_decision_boundary.executed.ipynb')

    pm.execute_notebook(input_notebook, output_notebook)

    input_notebook = os.path.join(
        current_folder, '02.candle_strategy_0400_forward_testing.ipynb')
    output_notebook = os.path.join(
        current_strategies, '02.candle_strategy_0400_forward_testing.executed.ipynb')

    pm.execute_notebook(input_notebook, output_notebook)


def run_scenarios(args):
    if args.minimum_interactions is None:
        print('In order to run the scenarios, we need to specify the --minimum-interactions parameter')
        sys.exit(1)

    MINIMUM_INTERACTIONS = int(args.minimum_interactions)

    os.environ["DATA_INPUT_DIR"] = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'input')
    for current_interaction in range(MINIMUM_INTERACTIONS):
        CURRENT_TARGET = os.environ['CURRENT_TARGET']
        CURRENT_STOP = os.environ['CURRENT_STOP']
        DECISION_BOUNDARY = os.environ['DECISION_BOUNDARY']
        print(
            f'Running Interaction ({current_interaction + 1}/{MINIMUM_INTERACTIONS}), Params: {CURRENT_TARGET} / {CURRENT_STOP} / {DECISION_BOUNDARY}')
        run_notebook()
