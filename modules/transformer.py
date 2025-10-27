import pandas as pd


def drop_nulls(df, columns = None):
    return df.dropna(subset=columns) if columns else df.dropna()

def drop_duplicated(df):
    return df.drop_duplicates()


def fill_missing(df, column, method, fixed_value=None):
    if method == "Fixed value" and fixed_value is not None:
        df[column].fillna(fixed_value, inplace=True)
    elif method in ["Mean", "Median"]:
        if pd.api.types.is_numeric_dtype(df[column]):
            if method == "Mean":
                df[column].fillna(df[column].mean(), inplace=True)
            else:
                df[column].fillna(df[column].median(), inplace=True)
        else:
            raise ValueError(f"Cannot use '{method}' on non-numeric column '{column}'")
    elif method == "Mode":
        df[column].fillna(df[column].mode()[0], inplace=True)
    return df