#!/bin/bash

source ./clean_notebooks.sh

export PYTHONPATH=$PWD

export PYAUTOTRADER_ROOT=$PWD

export USAR_SMART_STOP=0

poetry run python -m pyautotrader summarize_scenarios

cd pyautotrader/utils

poetry run python ./generate_pnl_charts.py

cd $PYAUTOTRADER_ROOT

cd models/strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies

cd $PYAUTOTRADER_ROOT

