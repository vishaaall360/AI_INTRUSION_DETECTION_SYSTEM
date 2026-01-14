import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    X = df.drop("label", axis=1)
    y = df["label"].map({"normal": 0, "attack": 1})
    return X, y
