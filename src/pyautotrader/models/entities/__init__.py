from sqlalchemy import Column, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, Text, String, Float

Base = declarative_base()


class QuoteORM(Base):

    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    exchange = Column(String(20), unique=False, nullable=False)
    asset = Column(String(20), unique=False, nullable=False)
    timeframe = Column(String(10), unique=False, nullable=False)
    date = Column(String(8), unique=False, nullable=False)
    time = Column(String(4), unique=False, nullable=False)
    open = Column(Float, unique=False, nullable=False)
    high = Column(Float, unique=False, nullable=False)
    low = Column(Float, unique=False, nullable=False)
    close = Column(Integer, unique=False, nullable=False)
    business = Column(Integer, unique=False, nullable=False)
    volume = Column(Integer, unique=False, nullable=False)


Index('idx_quote', QuoteORM.exchange, QuoteORM.asset,
      QuoteORM.timeframe, QuoteORM.date, QuoteORM.time, unique=True)
