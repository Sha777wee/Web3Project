from datetime import datetime

import requests

from common.data_engine import DataEngine
from common.object import TickData


class RuneEngine(DataEngine):
    def handle_tick_data(self, response: requests.Response) -> TickData:
        return TickData(symbol=self.symbol, datetime=datetime.now(), price=float(response["data"]["floor_price"]))
