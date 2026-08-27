from .card import Card

class PropertyCard(Card):
    def __init__(self, **kwargs):
        super().__init__(kwargs["Name"], "☐")
        self.info = kwargs


    def land_on(self, player):
        from player import Player

        print(player.all_info())

        if self.ownership:
            player.update_money(self.info["Rent"] * -1)
        else:
            purchase_decision = input(f"{player}... Buy {self.name} for {self.info["Price"]}? (Y/N): ")
            if purchase_decision.lower() == "y":
                player.update_money(self.info["Price"] * -1)

                self.ownership = player
                player.ownership.append(self)

    def __str__(self):
        return f"{self.name}, {self.info["Color"]}"

