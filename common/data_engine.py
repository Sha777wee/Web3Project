import json
from abc import abstractmethod

import requests

from common.object import TickData


class DataEngine:
    def __init__(self, symbol: str = None, url: str = None) -> None:
        self.symbol = symbol
        self.url = url

    def get_tick_data(self) -> TickData:
        response = requests.get(self.url)
        if response.status_code == 200:
            return self.handle_tick_data(json.loads(response.text))

    @abstractmethod
    def handle_tick_data(self, response: requests.Response) -> TickData:
        pass
