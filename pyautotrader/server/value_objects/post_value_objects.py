from pydantic import BaseModel


class Quote(BaseModel):
    date: str
    time: str
    open: float
    high: float
    low: float
    close: float
    business: float
    volume: float
