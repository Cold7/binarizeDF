#binarizer function
def binarize(df, threshold=0):
    for col in df.columns:
        df.loc[df[col] > threshold, col] = 1
    return df
