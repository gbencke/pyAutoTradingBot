import sys
from sqlalchemy import create_engine
from .entities import Base


def migrate_tables(args):
    if args.sqlalchemy_connection_string is None:
        print('In order to start the server, you need to specify the SQLAlchemy connection string...')
        sys.exit(1)

    engine = create_engine(args.sqlalchemy_connection_string)
    Base.metadata.create_all(engine)
