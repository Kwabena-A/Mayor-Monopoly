from .card import Card

class ActionCard(Card):
    def __init__(self, name, price, rent):
        super().__init__(name, "△")
        self.price = price
        self.rent = rent

    def land_on(self): # Dosent account for own player yet.
        print("You must jump 3 times.")
