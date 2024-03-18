import sys
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pyautotrader.models.entities import QuoteORM

def import_data_from_csv(args):
    if args.source is None:
        print('We need to specify the source file to import from...')
        sys.exit(1)
    if args.sqlalchemy_connection_string is None:
        print('In order to start the import, you need to specify the SQLAlchemy connection string...')
        sys.exit(1)

    if args.asset is None:
        print('We need to specify the asset that we are importing into...')
        sys.exit(1)
    if args.exchange is None:
        print('We need to specify the exchange that we are importing into...')
        sys.exit(1)
    if args.timeframe is None:
        print('We need to specify the timeframe that we are importing into...')
        sys.exit(1)

    if args.timeframe not in ['5Min', '10Min', '15Min', '30Min', '60Min', 'Daily']:
        print('Values for timeframe are: 5Min, 10Min, 15Min, 30Min, 60Min, Daily')
        sys.exit(1)

    csv_to_import = pd.read_csv(args.source)
    if not 'datetime' in csv_to_import.columns:
        print('The column datetime is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'open' in csv_to_import.columns:
        print('The column open is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'high' in csv_to_import.columns:
        print('The column high is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'low' in csv_to_import.columns:
        print('The column low is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'close' in csv_to_import.columns:
        print('The column close is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'business' in csv_to_import.columns:
        print('The column business is not present in the csv, we cannot continue...')
        sys.exit(1)
    if not 'volume' in csv_to_import.columns:
        print('The column volume is not present in the csv, we cannot continue...')
        sys.exit(1)

    engine = create_engine(args.sqlalchemy_connection_string)
    csv_to_import.reset_index()
    with Session(engine) as session:
        for index, row in csv_to_import.iterrows():
            try:
                datetime = row['datetime']
                if ' ' in datetime:
                    date = datetime.split(' ')[0]
                    time = datetime.split(' ')[1]
                else:
                    date = datetime.split(' ')[0]
                    time = '0000'

                date = date.replace(':', '').replace('.', '')
                time = time.replace(':', '').replace('.', '')

                quote_to_add = QuoteORM(exchange=args.exchange,
                                        asset=args.asset,
                                        timeframe=args.timeframe,
                                        date=date,
                                        time=time,
                                        open=row['open'],
                                        high=row['high'],
                                        low=row['low'],
                                        close=row['close'],
                                        business=row['business'],
                                        datetime=((int(date) * 10000) +
                                                  int(time)) - 201600000000,
                                        volume=row['volume'])
                session.add(quote_to_add)
            except IntegrityError as ex:
                pass
        session.commit()
