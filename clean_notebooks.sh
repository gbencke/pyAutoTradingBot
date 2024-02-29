#!/bin/bash

poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./models/strategies/B3/WDOL/02.candle_strategy/02.candle_strategy_0100_create_dataframe.ipynb
 
poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./models/strategies/B3/WDOL/02.candle_strategy/02.candle_strategy_0200_create_xgbooster.ipynb

poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./models/strategies/B3/WDOL/02.candle_strategy/02.candle_strategy_0300_find_decision_boundary.ipynb

poetry run jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./models/strategies/B3/WDOL/02.candle_strategy/02.candle_strategy_0400_forward_testing.ipynb

