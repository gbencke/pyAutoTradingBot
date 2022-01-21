#!/bin/bash

source ./env/bin/activate

source ./clean_notebooks.sh

export PYTHONPATH=$PWD/src

cd src/pyautotrader

python __main__.py run_scenarios --minimum-interactions 3

cd ../strategies/B3/WDOL/00.data/

export strategy7z="$(date '+%Y%m%d%H%M%S').strategies.7z"

7z a -mx9 $strategy7z strategies





