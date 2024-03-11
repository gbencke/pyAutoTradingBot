#!/bin/bash

export PYTHONPATH=pyautotrader

source ./clean_notebooks.sh

cd src/strategies/B3/WDOL/02.candle_strategy

poetry run jupyter nbconvert --inplace --to notebook --ExecutePreprocessor.timeout=-1 --execute 02.candle_strategy_0100_create_dataframe.ipynb
 
poetry run jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute 02.candle_strategy_0200_create_xgbooster.ipynb

poetry run jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute 02.candle_strategy_0300_find_decision_boundary.ipynb

poetry run jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute 02.candle_strategy_0400_forward_testing.ipynb

cd ../../../../..

source ./clean_notebooks.sh
