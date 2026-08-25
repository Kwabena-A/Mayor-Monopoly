from abc import ABC, abstractmethod
from player import Player

class Card(ABC):
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.ownership = None

    @abstractmethod
    def land_on(self, player: Player):
        pass

