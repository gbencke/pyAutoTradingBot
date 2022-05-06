cd %PYAUTOTRADER_ROOT%

set SOURCE_DIR=%cd%

set PYTHONPATH=\git\216\src

.\env\Scripts\activate.bat & cd utils & python import_data_from_profit.py


