from card import PropertyCard, ActionCard, Space

BOARD = [Space(x, PropertyCard(f"{x} bolevard", x * 10, x * 20)) for x in range(1, 41)]

for space in BOARD:
    print(space)