from .card import Card

class PropertyCard(Card):
    def __init__(self, name, price, rent):
        super().__init__(name, "☐")
        self.price = price
        self.rent = rent

    def land_on(self): # Dosent account for own player yet.
        if super().ownership == False:
            print("You can buy this property")
        else:
            print("You must pay rent")
