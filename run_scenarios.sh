#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

export PYAUTOTRADER_ROOT=$PWD

cd src/pyautotrader

export CURRENT_TARGET=1.2
export CURRENT_STOP=0.7
export CURRENT_5MIN_FILE_CSV='WDO$M10.csv'
export CURRENT_TIMEFRAME=10Min
export MAX_TRADE_DURATION=24
python __main__.py run_scenarios --minimum-interactions 2

python __main__.py summarize_scenarios

cd ../../utils

python ./generate_pnl_charts.py

cd $PYAUTOTRADER_ROOT

cd ../strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies

cd $PYAUTOTRADER_ROOT



