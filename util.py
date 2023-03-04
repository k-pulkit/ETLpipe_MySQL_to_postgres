import pandas as pd

def get_tables():
    tables = pd.read_csv('./tablelist.txt', sep=':').query('to_be_loaded=="yes"')
    return tables