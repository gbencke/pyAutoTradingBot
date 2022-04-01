set SOURCE_DIR=%cd%

call .\env\Scripts\activate.bat

set PYAUTOTRADER_ROOT=%cd%

set PYTHONPATH=C:\git\216\src

cd src\pyautotrader

python __main__.py  start_server --sqlalchemy-connection-string sqlite:///data//pyautotrader.db  --xgboost-model %PYAUTOTRADER_MODEL%

