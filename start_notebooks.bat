set SOURCE_DIR=%cd%

call .\env\Scripts\activate.bat

set PYTHONPATH=src
set USAR_SMART_STOP=0
set CURRENT_TARGET=0.8
set CURRENT_STOP=0.4
set CURRENT_5MIN_FILE_CSV=WDO$M5.csv
set CURRENT_TIMEFRAME=5Min
set MAX_TRADE_DURATION=24
set NUM_TREES=5
set TREE_DEPTH=1
set PYAUTOTRADER_URL=http://localhost:5000/
set DATA_OUTPUT_DIR=\git\216\src\strategies\B3\WDOL\00.data\output\

.\env\Scripts\activate.bat && jupyter lab --ip='*' --port=8080 --no-browser
