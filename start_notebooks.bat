set PYTHONPATH=src
set CURRENT_TARGET=0.9
set CURRENT_STOP=0.6
set CURRENT_5MIN_FILE_CSV=WDO$M10.csv
set CURRENT_TIMEFRAME=10Min
set MAX_TRADE_DURATION=24
set PYAUTOTRADER_URL=http://localhost:5000/
set DATA_OUTPUT_DIR=C:\git\216\src\strategies\B3\WDOL\00.data\output\

.\env\Scripts\activate.bat && jupyter lab --ip='*' --port=8080 --no-browser
