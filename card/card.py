from abc import ABC, abstractmethod
from player import Player

class Card(ABC):
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.ownership = None

    @abstractmethod
    def land_on(self, player: Player, roll: int):
        pass

    def pass_on(self, player: Player):
        print(f"{player.name} passed on me ({self.name})")

