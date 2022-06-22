set SOURCE_DIR=%cd%

call .\env\Scripts\activate.bat

set PYTHONPATH=src
set USAR_SMART_STOP=0
set PYAUTOTRADER_URL=http://localhost:5000/
set DATA_OUTPUT_DIR=\git\216\src\strategies\B3\WDOL\00.data\output\

.\env\Scripts\activate.bat && jupyter lab --ip='*' --port=8080 --no-browser
