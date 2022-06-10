

TIMEFRAMES = [{'timeframe':  '5Min',
               'file': 'WDO$M5.csv',  'tradeduration': 24}]

#CURRENT_TARGET = [1.1, 1.0, 0.9, 0.8, 0.7]
#CURRENT_STOP = [0.6, 0.5, 0.4, 0.3]
#DECISION_BOUNDARY = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]

CURRENT_TARGET = [0.8]
CURRENT_STOP = [0.4]
DECISION_BOUNDARY = [0.4]
WEIGHT_RATIO = [0.8, 1.0, 1.2]
NUM_TREES = list(range(1, 100))
TREE_DEPTH = [1, 2, 3]

totalScenariosRun = 0

print('#!/bin/bash\n')

print('source ./env/bin/activate\n')

print('source ./clean_notebooks.sh\n')

print('export PYTHONPATH=$PWD/src\n')

print('export PYAUTOTRADER_ROOT=$PWD\n')

print('export USAR_SMART_STOP=0\n')

print('cd src/pyautotrader\n')

for curWEIGHT_RATIO in WEIGHT_RATIO:
    for curNUM_TREE in NUM_TREES:
        for curTREE_DEPTH in TREE_DEPTH:
            for curTIMEFRAME in TIMEFRAMES:
                for curTARGET in CURRENT_TARGET:
                    for curSTOP in CURRENT_STOP:
                        for curDecisionBoundary in DECISION_BOUNDARY:
                            if curTARGET < (curSTOP * 2):
                                continue
                            totalScenariosRun += 1
                            print(f'export WEIGHT_RATIO={curWEIGHT_RATIO}')
                            print(f"export NUM_TREES={curNUM_TREE}")
                            print(f"export TREE_DEPTH={curTREE_DEPTH}")
                            print(f"export CURRENT_TARGET={curTARGET}")
                            print(f"export CURRENT_STOP={curSTOP}")
                            print(
                                f"export DECISION_BOUNDARY={curDecisionBoundary}")
                            print(
                                f"export CURRENT_5MIN_FILE_CSV='{curTIMEFRAME['file']}'")
                            print(
                                f"export CURRENT_TIMEFRAME={curTIMEFRAME['timeframe']}")
                            print(
                                f"export MAX_TRADE_DURATION={curTIMEFRAME['tradeduration']}")
                            print(
                                f"python __main__.py run_scenarios --minimum-interactions 1 & ")
                            print()
                            if (totalScenariosRun % 6) == 0:
                                print('wait')

print('wait\n')

print("python __main__.py summarize_scenarios\n")

print("cd ../../utils\n")

print("python ./generate_pnl_charts.py\n")

print("cd $PYAUTOTRADER_ROOT\n")

print("cd src/strategies/B3/WDOL/00.data/\n")

print('export strategy7z="$(date \'+%Y%m%d%H%M%S\').strategies.7z"\n')

print("7z a -mx9 $strategy7z strategies\n")

print("cd $PYAUTOTRADER_ROOT\n")
