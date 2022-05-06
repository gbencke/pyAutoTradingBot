#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

export PYAUTOTRADER_ROOT=$PWD

cd src/pyautotrader

export USAR_SMART_TOP=0

python __main__.py rerun_scenarios 

python __main__.py summarize_scenarios

cd ../../utils

python ./generate_pnl_charts.py

cd $PYAUTOTRADER_ROOT

cd src/strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies

cd $PYAUTOTRADER_ROOT


