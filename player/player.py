import card
from utils import count_color

class Player:
    def __init__(self, name: str, board_spaces):
        self.name = name
        self.board_spaces = board_spaces
        self.board_spaces: list[card.Space]
        self.location = 0
        self.ownership = []
        self.money = 1200
        self.update_location()
        self.status = "Active"
        self.jail_rolls = 0

    def update_location(self, move: int = 0, skip_over = False, move_to = ""):
        if isinstance(move_to, int):
            move = move_to
            skip_over = True
            move_to = ""
        if move_to != "":
            for space in self.board_spaces:
                print(space.card.name, " ", move_to)
                if move_to in space.card.name and "Go to " not in space.card.name:
                    print(space.location, " ", self.location)
                    if space.location > self.location:
                        move = space.location - self.location
                    else:
                        move = ((len(self.board_spaces) - self.location)
                                + space.location)
                    print(move)
                    break

        if skip_over:
            self.location = (self.location + move)
            if self.location >= len(self.board_spaces):
                self.location -= len(self.board_spaces)
        else:
            # Pass Over
            if move > 0:
                passed_count = 0
                while passed_count < move - 1:
                    passed_count += 1
                    self.location += 1
                    if self.location >= len(self.board_spaces):
                        self.location = 0
                    self.board_spaces[self.location].card.pass_on(self)
                self.location += 1
                if self.location >= len(self.board_spaces):
                    self.location = 0

        # Update board
        for space in self.board_spaces:
            if space.location == self.location:
                if self not in space.currentlyOn:
                    self.board_spaces[self.location].currentlyOn.append(self)
            else:
                if self in space.currentlyOn:
                    space.currentlyOn.remove(self)

        print(self.location)
        self.board_spaces[self.location].card.land_on(self)

    def update_money(self, amount: int):
        print(f'{self.money} -> {self.money + amount}')
        self.money += amount

    def all_info(self) -> str:
        return f"""
        | {self.name}
        | Money: {self.money}
        | Location: {self.location}
        | Ownership:\n{"\n".join([f"\t\t\t+ {x}" for x in self.ownership] )}
        """

    def upgrade_property(self, property):
        assert isinstance(property, card.PropertyCard), "Passed non-property"
        isUpgraded = False
        if property.ownership == self: # Confirm Ownership
            owned_color_count = 0
            for owned_property in self.ownership: # Count owned same colors
                if isinstance(owned_property, card.PropertyCard) and owned_property.info["Color"] == property.info["Color"]:
                    owned_color_count += 1
            if owned_color_count == count_color(property.info["Color"]): # Confirm full
                if self.money > property.info["PriceBuild"]:
                    self.update_money(property.info["PriceBuild"] * -1)
                    isUpgraded = property.upgrade_property()

        if isUpgraded:
            print(f"{self.name} upgraded {property}")
        else:
            print(f"{self.name} FAILED to upgrade {property}")

    def downgrade_property(self, property):
        assert isinstance(property, card.PropertyCard), "Passed non-property"
        isDowngraded = False
        if property.ownership == self: # Confirm Ownership
            if property.downgrade_property():
                self.update_money(property.info["PriceBuild"]) # Return Money
                isDowngraded = True

        if isDowngraded:
            print(f"{self.name} downgraded {property}")
        else:
            print(f"{self.name} FAILED to downgrade {property}")

    def leave_jail(self):
        self.update_money(-50)
        self.status = "Active"
        self.jail_rolls = 0

    def __str__(self):
        return self.name






