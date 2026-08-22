from .card import Card

class PropertyCard(Card):
    def __init__(self, **kwargs):
        print(kwargs)
        super().__init__(kwargs["Name"], "☐")
        self.info = kwargs


    def land_on(self): # Dosent account for own player yet.
        if super().ownership == False:
            print("You can buy this property")
        else:
            print("You must pay rent")
