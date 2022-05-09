

TIMEFRAMES = [{'timeframe':  '5Min',
               'file': 'WDO$M5.csv',  'tradeduration': 24}]

CURRENT_TARGET = [1.1, 1.0, 0.9, 0.8, 0.7]
CURRENT_STOP = [0.6, 0.5, 0.4, 0.3]
DECISION_BOUNDARY = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2]

for curTIMEFRAME in TIMEFRAMES:
    for curTARGET in CURRENT_TARGET:
        for curSTOP in CURRENT_STOP:
            for curDecisionBoundary in DECISION_BOUNDARY:
                if curTARGET < (curSTOP * 2):
                    continue
                print(f"export CURRENT_TARGET={curTARGET}")
                print(f"export CURRENT_STOP={curSTOP}")
                print(f"export DECISION_BOUNDARY={curDecisionBoundary}")
                print(f"export CURRENT_5MIN_FILE_CSV='{curTIMEFRAME['file']}'")
                print(f"export CURRENT_TIMEFRAME={curTIMEFRAME['timeframe']}")
                print(
                    f"export MAX_TRADE_DURATION={curTIMEFRAME['tradeduration']}")
                print(f"python __main__.py run_scenarios --minimum-interactions 1")
                print()
