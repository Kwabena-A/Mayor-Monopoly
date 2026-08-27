import pandas as pd
from card import PropertyCard, ActionCard, Space, ActionType

if __name__ == '__main__':
    df = pd.read_csv("../data/board.csv")
else:
    df = pd.read_csv("data/board.csv")

board_spaces = []

for x in range(df.shape[0]):
    if df.loc[x, 'Space'] == "Property":
        card = PropertyCard(**(df.loc[x].to_dict()))
    elif df.loc[x, 'Space'] == "Tax":
        card = ActionCard(df.loc[x, "Name"],
                          ActionType(df.loc[x, "Price"]))
    else:
        card = ActionCard(df.loc[x, 'Name'], "10")
    board_spaces.append(Space(len(board_spaces), card))

if __name__ == '__main__':
    print(*board_spaces)

