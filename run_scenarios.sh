#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

export PYAUTOTRADER_ROOT=$PWD

export USAR_SMART_STOP=0

cd src/pyautotrader

export WEIGHT_RATIO=0.8
export NUM_TREES=1
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=2
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=3
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=4
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=5
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=6
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=7
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=8
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=9
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=10
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=11
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=12
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=13
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=14
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=15
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=16
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=17
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=18
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=19
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=20
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=21
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=22
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=23
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=24
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=25
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=26
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=27
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=28
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=29
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=30
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=31
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=32
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=33
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=34
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=35
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=36
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=37
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=38
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=39
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=40
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=41
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=42
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=43
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=44
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=45
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=46
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=47
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=48
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=49
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=50
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=51
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=52
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=53
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=54
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=55
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=56
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=57
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=58
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=59
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=60
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=61
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=62
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=63
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=64
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=65
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=66
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=67
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=68
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=69
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=70
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=71
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=72
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=73
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=74
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=75
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=76
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=77
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=78
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=79
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=80
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=81
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=82
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=83
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=84
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=85
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=86
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=87
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=88
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=89
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=90
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=91
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=92
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=93
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=94
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=95
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=96
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

wait
export WEIGHT_RATIO=0.8
export NUM_TREES=97
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=98
export TREE_DEPTH=2
export CURRENT_TARGET=0.8
export CURRENT_STOP=0.4
export DECISION_BOUNDARY=0.4
export CURRENT_5MIN_FILE_CSV='WDO$M5.csv'
export CURRENT_TIMEFRAME=5Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 1 & 

export WEIGHT_RATIO=0.8
export NUM_TREES=99
export TREE_DEPTH=2
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

