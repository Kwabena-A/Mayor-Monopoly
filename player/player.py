from card import Space

class Player:
    def __init__(self, name: str, board_spaces: list[Space]):
        self.name = name
        self.board_spaces = board_spaces
        self.location = 0
        self.update_location()

        self.money = 8000

    def update_location(self, move: int = 0):
        self.location += move

        for space in self.board_spaces:
            if space.location == self.location:
                if self not in space.currentlyOn:
                    self.board_spaces[self.location].currentlyOn.append(self)
            else:
                if self in space.currentlyOn:
                    space.currentlyOn.remove(self)

    def add_money(self, amount: int):
        self.money += int
    def sub_money(self, amount: int):
        self.money -= int

