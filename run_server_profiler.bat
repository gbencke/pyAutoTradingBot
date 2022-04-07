call .\env\Scripts\activate.bat

set PYTHONPATH=%cd%\src

cd src\pyautotrader

python -m cProfile -o saida.out __main__.py start_server --sqlalchemy-connection-string sqlite:///data//pyautotrader.db --xgboost-model C:\git\216\src\strategies\B3\WDOL\00.data\output

