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

def count_invalid_values(
        df:pd.DataFrame, 
        table_name:str,
        missing_value_fillers:dict,
        dtypes_to_check:list,
        default_invalid_values:list=[""]
    ) -> pd.DataFrame:
    '''
    Counts the number of invalid values for each column in a table.

    Args:
        - df: Table to analyse
        - table_name: Name of the table for labeling results
        - missing_value_fillers: A dictionary where keys are column names and values are lists of invalid values.
                                Example: {"column1": ["99", "98"], "column2": ["Unknown"]}
        - dtypes_to_check: List of dtypes to include in the analysis
        - default_invalid_values: Default list of invalid values to check for columns not in `missing_value_fillers`.
    
    Returns: 
        - pd.DataFrame with a single column of invalid value counts for each row in the table
    '''
    if missing_value_fillers is None:
        missing_value_fillers = {}

    value_counts = {}
    for column in df.columns:
        if df[column].dtype in dtypes_to_check:
            # Get invalid values specific to the column
            invalid_values = missing_value_fillers.get(column, default_invalid_values)
            # Count invalid values
            value_counts[column] = df[column].isin(invalid_values).sum()
        else:
            # Default to 0 for columns not in the specified dtypes
            value_counts[column] = 0

    return pd.DataFrame.from_dict(value_counts, orient="index", columns=[table_name])

# TODO: Function to help sense check if a field contains invalid values

# TODO: Completeness table