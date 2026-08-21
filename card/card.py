from abc import ABC, abstractmethod

class Card(ABC):
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name
        self.ownership = ""

    @abstractmethod
    def land_on(self):
        pass
