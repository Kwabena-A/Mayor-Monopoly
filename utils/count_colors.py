import pandas as pd

df = pd.read_csv("data/board.csv")
def count_color(color: str) -> int:
    return (df[df["Color"] == color]).shape[0]