set PYTHONPATH=src

call .\env\Scripts\activate.bat 

call .\clean_notebooks.bat

jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0100_create_dataframe.ipynb
 
jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0200_create_xgbooster.ipynb

jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0300_find_decision_boundary.ipynb

jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute .\src\strategies\B3.WDOL\02.candle_strategy\02.candle_strategy_0400_forward_testing.ipynb

call .\clean_notebooks.bat
