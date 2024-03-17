########################################################
# BEFORE running this script                           #
# make sure that there is a trained XGBoost Model in   #
# models/strategies/B3/WDOL/00.data/output             #
########################################################

export SOURCE_DIR=$PWD

export PYAUTOTRADER_ROOT=$PWD

export PYTHONPATH=$PYTHONPATH:$PWD

export PYAUTOTRADER_MODEL=../models/strategies/B3/WDOL/00.data/output

cd pyautotrader || exit

poetry run python __main__.py  start_server --sqlalchemy-connection-string sqlite:///data//pyautotrader.db  --xgboost-model $PYAUTOTRADER_MODEL


