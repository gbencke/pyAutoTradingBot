export PYTHONPATH=src

source ./env/bin/activate && jupyter lab --ip='*' --port=8080 --no-browser
