#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

export PYAUTOTRADER_ROOT=$PWD

export USAR_SMART_STOP=0

cd src/pyautotrader

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.6
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.1
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.5
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=1.0
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.5
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.6
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.8
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.9
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.0
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.1
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

export CURRENT_TARGET=0.9
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=1.2
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=48
python __main__.py run_scenarios --minimum-interactions 1

python __main__.py summarize_scenarios

cd ../../utils

python ./generate_pnl_charts.py

cd $PYAUTOTRADER_ROOT

cd src/strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies

cd $PYAUTOTRADER_ROOT



