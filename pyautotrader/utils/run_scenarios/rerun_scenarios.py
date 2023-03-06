import os
import sys
import shutil
import papermill as pm


def rerun_scenarios():
    if not 'PYAUTOTRADER_ROOT' in os.environ:
        print('You need to set the PYAUTOTRADER_ROOT to rerun the scenarios...')
        sys.exit(1)

    strategies_folder = os.path.join(
        os.environ['PYAUTOTRADER_ROOT'], 'src', 'strategies', 'B3', 'WDOL', '00.data', 'strategies')
    if not os.path.isdir(strategies_folder):
        print(f'{strategies_folder} was not found...')
        sys.exit(1)

    os.environ['DATA_INPUT_DIR'] = os.path.join(
        os.environ['PYAUTOTRADER_ROOT'], 'src', 'strategies', 'B3', 'WDOL', '00.data', 'input')

    updated_notebook = os.path.join(os.environ['PYAUTOTRADER_ROOT'], 'src', 'strategies',
                                    'B3', 'WDOL', '02.candle_strategy', '02.candle_strategy_0400_forward_testing.ipynb')

    for current_strategy in os.listdir(strategies_folder):
        if not current_strategy.startswith("2"):
            continue
        strategy_folder = os.path.join(strategies_folder, current_strategy)
        os.environ['DATA_OUTPUT_DIR'] = strategy_folder

        input_notebook = os.path.join(
            strategy_folder, '02.candle_strategy_0400_forward_testing.ipynb')
        output_notebook = os.path.join(
            strategy_folder, '02.candle_strategy_0400_forward_testing.executed.ipynb')

        shutil.copyfile(updated_notebook, input_notebook)

        pm.execute_notebook(input_notebook, output_notebook)

        os.remove(input_notebook)
