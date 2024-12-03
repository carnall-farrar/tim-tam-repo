import pandas as pd

MISSING_VALUE_FILLERS = {
    # Dictionary where the keys are the names of the tables and the values are
    # a list of all characters that denote invalid values, e.g. '99'
}

def count_missing_values(df:pd.DataFrame, table_name:str) -> pd.DataFrame:
    '''
    This function counts the number of null values in each column of the df.

    Args:
        df: Table to analyse
        table_name: The table name
    
    Return: 
        pd.DataFrame: A single-column table where the column header is the 
        table name, the index consists of the input table's columns, and 
        the values represent the count of null values.
    '''
    return pd.DataFrame(df.isna().sum(), columns=[table_name])

def count_invalid_values(df:pd.DataFrame, table_name:str) -> pd.DataFrame:
    '''
    
    '''