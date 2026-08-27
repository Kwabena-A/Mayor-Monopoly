import pandas as pd
from card import ActionType

if __name__ == '__main__':
    df = pd.read_csv("../data/cards.csv", sep="|")
else:
    df = pd.read_csv("data/cards.csv", sep="|")

df.drop(columns=["tag"], inplace=True)

df_chance = df[df["type"] == "Chance"]
df_community = df[df["type"] == "Community Chest"].reset_index()


def init_list(active_df: pd.DataFrame) -> list:
    output = []
    for x in range(active_df.shape[0]):
        net = active_df.loc[x, "effect"]
        shared = active_df.loc[x, "category"] == "money_player"
        move_to = ""
        if "Advance to " in str(active_df.loc[x, "name"]):
            statement = (active_df.loc[x, "name"])
            if "nearest " in statement:
                move_to = statement[len("Advance to nearest "):]
            else:
                move_to = statement[len("Advance to "):]
            if "Jail" in move_to:
                move_to = "Jail"
            if move_to[-1] == ".":
                move_to = move_to[:-1]
        set_status = ""

        if "Jail" in str(active_df.loc[x, "name"]) != -1:
            set_status = "in jail"

        output.append(ActionType(net, shared, move_to, set_status))
    return output

chances = init_list(df_chance)
community = init_list(df_community)