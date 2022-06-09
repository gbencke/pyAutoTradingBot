#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

export PYAUTOTRADER_ROOT=$PWD

export USAR_SMART_STOP=0

cd src/pyautotrader

export NUM_TREES=1
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=2
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=3
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=4
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export NUM_TREES=5
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=6
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=7
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=8
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export NUM_TREES=9
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=10
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=11
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=12
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export NUM_TREES=13
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=14
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=15
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=16
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export NUM_TREES=17
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=18
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=19
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export NUM_TREES=20
export TREE_DEPTH=1
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait

python __main__.py summarize_scenarios

cd ../../utils

python ./generate_pnl_charts.py

cd $PYAUTOTRADER_ROOT

cd src/strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies

cd $PYAUTOTRADER_ROOT

