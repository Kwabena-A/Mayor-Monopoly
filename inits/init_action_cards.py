import pandas as pd
from card import ActionType

if __name__ == '__main__':
    df = pd.read_csv("../data/cards.csv", sep="|")
else:
    df = pd.read_csv("data/cards.csv", sep="|")

df.drop(columns=["tag"], inplace=True)

df_chance = df[df["type"] == "Chance"]
df_community = df[df["type"] == "Community Chest"].reset_index()


def init_list(active_df: pd.DataFrame) -> list[ActionType]:
    output = []
    for x in range(active_df.shape[0]):
        name = str(active_df.loc[x, "name"])
        if name[-1] == ".":
            name = name[:len(name) - 1]

        category = str(active_df.loc[x, "category"])

        net = active_df.loc[x, "effect"]
        shared = category == "money_player"
        move_to = ""
        set_status = ""
        ownable = False
        if "Get out of Jail Free" in name:
            set_status = "Active"
            ownable = True

        print(category)
        if "move" in category:
            net = 0
            print("Its a move card")
            if "rr" in category:
                move_to = "Railroad"
            elif "utility" in category:
                move_to = "Utility"
            elif "jail" in category:
                move_to = "Jail"
                set_status = "Jail"
            elif "abs" in category:
                move_to = -3
            else:
                board_spaces = pd.read_csv("data/board.csv")["Name"].to_list()

                splited = name.split(" ")
                merged = ""
                for x in reversed(range(len(splited))):
                    selected = " ".join(splited[x:])

                    for space in board_spaces:
                        print(f"{space} is {selected} check...")
                        if space == selected:
                            move_to = space
                            break
                    if move_to != "":
                        break

        output.append(ActionType(name, net, shared, move_to, set_status, ownable))
    return output

chances = init_list(df_chance)
community = init_list(df_community)

print("\n".join([x.full_info() for x in chances]))