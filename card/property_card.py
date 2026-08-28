from .card import Card

class PropertyCard(Card):
    def __init__(self, **kwargs):
        super().__init__(kwargs["Name"], "☐")
        self.info = kwargs
        self.info["RentBuild0"] = self.info["Rent"]
        self.house_count = 0


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
        return False

    def __str__(self):
        return f"{self.name}, {self.info["Color"]}"

