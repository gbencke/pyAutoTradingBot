import os
import sys
import papermill as pm
from datetime import datetime


def run_notebook():
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")

    current_folder = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '02.candle_strategy')
    current_strategies = os.path.join(
        os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'strategies')

    os.mkdir(os.path.join(current_strategies, current_date))
    current_strategies = os.path.join(current_strategies, current_date)

    os.environ["DATA_OUTPUT_DIR"] = current_strategies

    input_notebook = os.path.join(
        current_folder, '02.candle_strategy_0100_create_dataframe.ipynb')
    output_notebook = os.path.join(
        current_strategies, '02.candle_strategy_0100_create_dataframe.executed.ipynb')

    pm.execute_notebook(input_notebook, output_notebook)

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
    MINIMUM_TIME = ['930']
    MAXIMUM_TIME = ['1430']
    MINIMUM_DATE_DATAFRAME = ['20200101']
    MINIMUM_DATE_TRADE = ['20200110']
    MAX_TRAIN_DATE = ['20211027']
    MAX_TRADE_DURATION = ['24']
    CURRENT_TARGET = ['1.0']
    CURRENT_STOP = ['0.5']
    DECISION_BOUNDARY = ['0.4']

    for current_minimum_time in MINIMUM_TIME:
        for current_maximum_time in MAXIMUM_TIME:
            for current_minimum_date_dataframe in MINIMUM_DATE_DATAFRAME:
                for current_minimum_date_trade in MINIMUM_DATE_TRADE:
                    for current_max_train_date in MAX_TRAIN_DATE:
                        for current_max_trade_duration in MAX_TRADE_DURATION:
                            for current_target in CURRENT_TARGET:
                                for current_stop in CURRENT_STOP:
                                    for current_decision_boundary in DECISION_BOUNDARY:
                                        os.environ["MINIMUM_TIME"] = current_minimum_time
                                        os.environ["MAXIMUM_TIME"] = current_maximum_time
                                        os.environ["MINIMUM_DATE_DATAFRAME"] = current_minimum_date_dataframe
                                        os.environ["MINIMUM_DATE_TRADE"] = current_minimum_date_trade
                                        os.environ["MAX_TRAIN_DATE"] = current_max_train_date
                                        os.environ["MAX_TRADE_DURATION"] = current_max_trade_duration
                                        os.environ["CURRENT_TARGET"] = current_target
                                        os.environ["CURRENT_STOP"] = current_stop
                                        os.environ["DECISION_BOUNDARY"] = current_decision_boundary
                                        os.environ["DATA_INPUT_DIR"] = os.path.join(
                                            os.getcwd(), '..', 'strategies', 'B3', 'WDOL', '00.data', 'input')
                                        for current_interaction in range(MINIMUM_INTERACTIONS):
                                            run_notebook()
