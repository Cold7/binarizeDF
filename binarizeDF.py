#binarizer function
def binarize(df, threshold=0):
    for col in df.columns:
        df2.loc[df2[col] < threshold, col] = 0
        df.loc[df[col] > threshold, col] = 1
    return df
