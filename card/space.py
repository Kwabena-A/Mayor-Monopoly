from .card import Card

class Space:
    def __init__(self, location: int, card: Card):
        self.location = location
        self.currentlyOn = []

        self.card = card

    def __str__(self):
        return f"""
        --------
        {self.card.symbol}
        {self.card.name}
        --------
        """
