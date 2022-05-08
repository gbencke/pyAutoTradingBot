set PYTHONPATH=src

call .\env\Scripts\activate.bat 

call .\clean_notebooks.bat

set PYTHONPATH=src
set USAR_SMART_STOP=0
set CURRENT_TARGET=1.0
set CURRENT_STOP=0.4
set CURRENT_5MIN_FILE_CSV=WDO$M5.csv
set CURRENT_TIMEFRAME=5Min
set MAX_TRADE_DURATION=48
set PYAUTOTRADER_URL=http://localhost:5000/
set DATA_OUTPUT_DIR=\git\216\src\strategies\B3\WDOL\00.data\output\

jupyter nbconvert --inplace --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0100_create_dataframe.ipynb
 
jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0200_create_xgbooster.ipynb

jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0300_find_decision_boundary.ipynb

jupyter nbconvert --inplace  --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0400_forward_testing.ipynb

call .\clean_notebooks.bat
