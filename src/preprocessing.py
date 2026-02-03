def clean_data(df):
    return df.dropna()

def clean_data(df):
    """
    Elimina valores nulos del dataset
    """
    return df.dropna()

def normalize_columns(df):
    """
    Normaliza columnas numéricas entre 0 y 1
    """
    return (df - df.min()) / (df.max() - df.min())
