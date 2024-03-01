from dataclasses import dataclass

import datetime


@dataclass
class TickData:
    symbol: str
    datetime: datetime
    price: float = 0

