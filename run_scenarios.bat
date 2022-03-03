set SOURCE_DIR=%cd%

call .\env\Scripts\activate.bat

call .\clean_notebooks.bat

set PYTHONPATH=C:\git\216\src

echo %PYTHONPATH%

cd %SOURCE_DIR%

cd src\pyautotrader


set CURRENT_TARGET=0.8
set CURRENT_STOP=0.4

set CURRENT_5MIN_FILE_CSV=WDO$M5.csv
set CURRENT_TIMEFRAME=5Min
set MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 2

set CURRENT_5MIN_FILE_CSV=WDO$M10.csv
set CURRENT_TIMEFRAME=10Min
set MAX_TRADE_DURATION=12
python __main__.py run_scenarios --minimum-interactions 2

set CURRENT_5MIN_FILE_CSV=WDO$M15.csv
set CURRENT_TIMEFRAME=15Min
set MAX_TRADE_DURATION=8
python __main__.py run_scenarios --minimum-interactions 2

rem ------------------------------------------------------
python __main__.py summarize_scenarios

cd ..\strategies\B3\WDOL\00.data

set strategy7z=%date:~10,4%%date:~7,2%%date:~4,2%%time:~0,2%%time:~3,2%%time:~6,2%%time:~9,2%.strategy.7z

7z a -mx9 %strategy7z% strategies





