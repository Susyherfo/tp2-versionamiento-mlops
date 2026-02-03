import pandas as pd

def load_data(path):
    """
    Carga un dataset desde un archivo CSV
    """
    df = pd.read_csv(path)
    return df

def validate_data(df):
    """
    Validación básica del dataset
    """
    return not df.empty

def get_basic_info(df):
    """
    Retorna información básica del dataset
    """
    return df.describe()