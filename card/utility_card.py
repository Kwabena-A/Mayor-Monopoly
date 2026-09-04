from .card import Card
from utils import count_color
from .property_card import PropertyCard


class UtilityCard(PropertyCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.symbol = "U"
        self.util_multi = False


    def land_on(self, player, roll):
        self.update_rent(player)
        if self.util_multi:
            self.info["Rent"] = roll * 10
        else:
            self.info["Rent"] = roll * 4

        super().land_on(player, roll)

    def update_rent(self, _):
        from player import Player

        if self.ownership:
            util_count = 0
            for property in self.ownership.ownership:
                property: Card
                if isinstance(property, UtilityCard):
                    util_count += 1

            self.util_multi = util_count == 2

    def upgrade_property(self) -> bool:
        if self.house_count == -1:
            print(f"{self.name} (house count): {self.house_count} -> {self.house_count + 1}")

            self.house_count += 1
            self.info["Rent"] = self.info[f"RentBuild{self.house_count}"]
            return True
        return False

    def downgrade_property(self) -> bool:
        if self.house_count == 0:
            print(f"{self.name} (house count): {self.house_count} -> -1 (Mortgaged)")
            self.house_count -= 1
            self.info["Rent"] = 0
            return True
        return False

    def __str__(self):
        return f"{self.name} [{self.info["Color"]}] [{self.info["Rent"]}]"

