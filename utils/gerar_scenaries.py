

TIMEFRAMES = [{'timeframe': '10Min', 'file': 'WDO$M10.csv', 'tradeduration': 24},
              {'timeframe':  '5Min', 'file': 'WDO$M5.csv',  'tradeduration': 48}]

CURRENT_TARGET = [1.0, 0.9, 0.8, 0.7,0.6,0.5, 0.4]
CURRENT_STOP = [0.6,0.5,0.4, 0.3]

for curTIMEFRAME in TIMEFRAMES:
    for curTARGET in CURRENT_TARGET:
        for curSTOP in CURRENT_STOP:
            print(f"export CURRENT_TARGET={curTARGET}")
            print(f"export CURRENT_STOP={curSTOP}")
            print(f"export CURRENT_5MIN_FILE_CSV='{curTIMEFRAME['file']}'")
            print(f"export CURRENT_TIMEFRAME={curTIMEFRAME['timeframe']}")
            print(f"export MAX_TRADE_DURATION={curTIMEFRAME['tradeduration']}")
            print(f"python __main__.py run_scenarios --minimum-interactions 20")
            print()
