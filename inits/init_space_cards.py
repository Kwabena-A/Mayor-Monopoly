import pandas as pd
from card import PropertyCard, ActionCard, Space, ActionType, RailroadCard
from card.utility_card import UtilityCard
from .init_action_cards import chances, community

if __name__ == '__main__':
    df = pd.read_csv("../data/board.csv")
else:
    df = pd.read_csv("data/board.csv")

board_spaces = []

for x in range(df.shape[0]):
    if df.loc[x, 'Space'] == "Property":
        card = PropertyCard(**(df.loc[x].to_dict()))
    elif df.loc[x, 'Space'] == "Railroad":
        card = RailroadCard(**(df.loc[x].to_dict()))
    elif df.loc[x, 'Space'] == "Utility":
        card = UtilityCard(**(df.loc[x].to_dict()))
    elif df.loc[x, 'Space'] == "Go":
        card = ActionCard(df.loc[x, "Name"], ActionType(str(df.loc[x, "Name"]), 200), isPassOnAction=True)
    elif df.loc[x, 'Space'] == "GoToJail":
        card = ActionCard(df.loc[x, "Name"], ActionType(str(df.loc[x, "Name"]), move_to="Jail", set_status="Jail"))
    elif df.loc[x, 'Space'] == "Tax":
        card = ActionCard(df.loc[x, "Name"],
                          ActionType(str(df.loc[x, "Name"]), net=df.loc[x, "Price"] * -1))
    elif df.loc[x, 'Space'] == "Chance":
        card = ActionCard("Chance",
                          chances)
    elif df.loc[x, 'Space'] == "Chest":
        card = ActionCard("Community Chest",
                          community)
    else:
        card = ActionCard(df.loc[x, 'Name'], "10")


    board_spaces.append(Space(len(board_spaces), card))

if __name__ == '__main__':
    print(*board_spaces)

