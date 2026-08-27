import card


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

    def update_location(self, move: int = 0, skip_over = False, move_to: str = ""):
        if move_to != "":
            for space in self.board_spaces:
                if move_to in space.card.name:
                    if space.location > self.location:
                        move = space.location - self.location
                    else:
                        move = (self.location
                                + (len(self.board_spaces) - self.location)
                                + space.location)

        if skip_over:
            self.location = move
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

        # Update board
        for space in self.board_spaces:
            if space.location == self.location:
                if self not in space.currentlyOn:
                    self.board_spaces[self.location].currentlyOn.append(self)
            else:
                if self in space.currentlyOn:
                    space.currentlyOn.remove(self)

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

    def __str__(self):
        return self.name






