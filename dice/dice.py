import random


class Dice:
    def __init__(self, count: int):
        self.faces = "⚀ ⚁ ⚂ ⚃ ⚄ ⚅".split(" ")
        self.count = count

    def roll(self) -> tuple[int, bool]:
        rolled_faces = []
        rolled_count = 0
        for x in range(self.count):
            rolled = random.randint(1,6)
            rolled_faces.append(self.faces[rolled - 1])
            rolled_count += rolled
        print(" ".join(rolled_faces), " = ", rolled_count)
        return (rolled_count, True) if rolled_faces[0] * self.count == rolled_faces else (rolled_count, False)


