from .card import Card
class ActionCard(Card):
    def __init__(self, name, price, rent):
        super().__init__(name, "△")
        self.price = price
        self.rent = rent

    def land_on(self, player): # Dosent account for own player yet.
        from player import Player
        print("Jump three times")

