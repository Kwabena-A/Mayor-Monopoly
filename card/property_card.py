from .card import Card

class PropertyCard(Card):
    def __init__(self, **kwargs):
        super().__init__(kwargs["Name"], "☐")
        self.info = kwargs


    def land_on(self, player):
        from player import Player

        print(player.all_info())

        if self.ownership:
            print(f'{player.money} -> {player.money - self.info["Rent"]}')
            player.sub_money(self.info["Rent"])
        else:
            purchase_decision = input(f"{player}... Buy {self.name} for {self.info["Price"]}? (Y/N): ")
            if purchase_decision.lower() == "y":
                print(f'{player.money} -> {player.money - self.info["Price"]}')
                player.sub_money(self.info["Price"])

                self.ownership = player
                player.ownership.append(self)

    def __str__(self):
        return f"{self.name}, {self.info["Color"]}"

