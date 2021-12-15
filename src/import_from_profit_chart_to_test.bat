@echo off
call ..\env\Scripts\activate
set PYTHONPATH=C:\git\216\srv

del C:\git\216\src\strategies\B3.WDOL\00.data\input\WDO$M5_test.csv
del C:\git\216\src\strategies\B3.WDOL\00.data\input\WDO$Daily_test.csv

python -m pyautotrader import_data_from_profit_chart_into_metatrader --source "C:\git\216\src\strategies\B3.WDOL\00.data\input\WDOFUT_F_0_5Min.csv" --destination "C:\git\216\src\strategies\B3.WDOL\00.data\input\WDO$M5_test.csv" --initial-date "2020.01.29"
python -m pyautotrader import_data_from_profit_chart_into_metatrader --source "C:\git\216\src\strategies\B3.WDOL\00.data\input\WDOFUT_F_0_Diario.csv" --destination "C:\git\216\src\strategies\B3.WDOL\00.data\input\WDO$Daily_test.csv" --initial-date "2020.01.29"



