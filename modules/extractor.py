import pandas as pd

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def read_json(path: str) -> pd.DataFrame:
    return pd.read_json(path)

def read_excel(path: str) -> pd.DataFrame:
    return pd.read_excel(path)