#binarizer function
def binarize(df, threshold=0):
    df2 = df.copy()
    for col in df.columns:
        df2.loc[df2[col] < threshold, col] = 0
        df2.loc[df2[col] > threshold, col] = 1
    return df2
