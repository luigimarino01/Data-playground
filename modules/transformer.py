def drop_nulls(df, columns = None):
    return df.dropna(subset=columns) if columns else df.dropna()

def drop_duplicated(df):
    return df.drop_duplicates()


