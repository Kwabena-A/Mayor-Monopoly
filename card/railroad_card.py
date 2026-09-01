from .card import Card
from utils import count_color
from .property_card import PropertyCard


class RailroadCard(PropertyCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def update_rent(self, player):
        from player import Player

        assert isinstance(player, Player), "Non-player passed"
        assert self in player.ownership, "Assinged in correct player"

        rent = 25
        for property in player.ownership:
            property: Card
            if isinstance(property, RailroadCard):
                rent *= 2

        self.info["Rent"] = rent

    def __str__(self):
        return f"{self.name} [{self.info["Color"]}] [{self.info["Rent"]}]"

