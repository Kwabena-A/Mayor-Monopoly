from .card import Card
from utils import count_color


class PropertyCard(Card):
    def __init__(self, **kwargs):
        super().__init__(kwargs["Name"], "☐")
        self.info = kwargs
        self.info["RentBuild0"] = self.info["Rent"]
        self.house_count = 0


    def land_on(self, player, roll):
        from player import Player
        from .railroad_card import RailroadCard

        assert isinstance(player, Player)

        print(player.all_info())

        if self.ownership:
            if self not in player.ownership:
                player.update_money(self.info["Rent"] * -1)
        else:
            purchase_decision = input(f"{player}... Buy {self.name} for {self.info["Price"]}? (Y/N): ")
            if purchase_decision.lower() == "y":
                player.update_money(self.info["Price"] * -1)

                self.ownership = player
                player.ownership.append(self)
                self.update_rent(player)
                for railroad in [x for x in player.ownership if isinstance(x, RailroadCard)]:
                    railroad.update_rent(player)

    def update_rent(self, player):
        if self.house_count > 0:
            self.info["Rent"] = self.info[f"RentBuild{self.house_count}"]
            return

        # All color combo check

        owned_color_count = 0
        for property in [x for x in player.ownership if isinstance(x, PropertyCard)]:
            if property.info["Color"] == self.info["Color"] and property.house_count != -1:
                owned_color_count += 1

        if owned_color_count == count_color(self.info["Color"]):
            self.info["Rent"] = self.info[f"RentBuild0"] * 2
            return

        self.info["Rent"] = self.info[f"RentBuild{self.house_count}"]

    def upgrade_property(self) -> bool:
        if self.house_count < 5:
            print(f"{self.name} (house count): {self.house_count} -> {self.house_count + 1}")

            self.house_count += 1
            self.info["Rent"] = self.info[f"RentBuild{self.house_count}"]
            return True


        return False

    def downgrade_property(self) -> bool:
        if self.house_count > 0:
            print(f"{self.name} (house count): {self.house_count} -> {self.house_count - 1}")

            self.house_count -= 1
            self.info["Rent"] = self.info[f"RentBuild{self.house_count}"]
            return True

        elif self.house_count == 0:
            print(f"{self.name} (house count): {self.house_count} -> -1 (Mortgaged)")
            self.house_count -= 1
            self.info["Rent"] = 0
            return True

        return False

    def __str__(self):
        return f"{self.name} [{self.info["Color"]}] [{self.info["Rent"]}] [{self.house_count}]"

