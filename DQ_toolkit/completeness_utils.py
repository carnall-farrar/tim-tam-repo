import pandas as pd
from timtam.utils import get_processed_path

MISSING_VALUE_FILLERS = {
    # column_1 : [list_of_invalid_values],
    # column_2 : [list_of_invalid_values]
}

INGESTION_FUNCTION = "ingestion_function"

ALL_TABLES = {
    # Nested dictionary where each entry is:
    # table_name: {INGESTION_FUNCTION: function to ingest table}
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

def values_sense_check(df:pd.DataFrame, print_output:bool=True) -> dict:
    ''' 
    Looks to identify potential invalid values in a column by looking at unique value counts.

    Args:
        - df: Table to analyse
        - print_output: A boolean which determines whether to print results while running the function. 
            Default is set to True.

    Retruns: 
        - dict: A dictionary containing the unique value counts and their frequencies for each column.
    '''
    column_counts = {}
    for column in df.columns:
        unique_count = df[column].nunique()
        value_counts = df[column].value_counts(dropna=False)

        column_counts[column] = {
            "nunique": unique_count,
            "value_counts": value_counts
        }
    # Print results in a readable format
    if print_output:
        print("Invalid value analysis")
        print("-" * 40)
        for column, stats in column_counts.items():
            print(f"Column: {column}")
            print(f"Number of unique values: {stats['nunique']}")
            print("Value counts:")
            print(stats["value_counts"])
            print("-" * 40)
    return column_counts

def check_table_completeness():
    '''
    Runs through all input tables and checks completeness, invalid values, and performs
    a sense check of the values in the tables.
    '''
    df_missing_values = pd.DataFrame
    df_invalid_values = pd.DataFrame
    dict_value_sense_check = {}

    for key, value in ALL_TABLES.items():
        df = value[INGESTION_FUNCTION]()
        df = df.drop_duplicates(ignore_index=True)
        print(f"------------------------Table: {key}---------------------")
        print(df.dtypes)
        print(f"Number of rows: {df.shape[0]}")
        df_missing_values = pd.merge(
            df_missing_values,
            count_missing_values(df, key),
            left_index=True,
            right_index=True,
            how="outer",
        )
        df_invalid_values = pd.merge(
            df_invalid_values,
            count_invalid_values(df, key),
            left_index=True,
            right_index=True,
            how="outer",
        )
        value_sense_check_results = values_sense_check(df, print_output=False)
        dict_value_sense_check[key] = value_sense_check_results
    
    # Save missing and invalid values
    df_missing_values.to_csv(get_processed_path("dq_missing_values.csv"), index=False)
    df_invalid_values.to_csv(get_processed_path("dq_invalid_values.csv"), index=False)

    # Flatten sense check outputs and save
    flat_sense_check = []
    for table, columns in dict_value_sense_check.items():
        for column, stats in columns.items(): 
            flat_sense_check.append({
                "table": table,
                "column": column,
                "nunique": stats["nunique"],
                "value_counts": stats["value_counts"].to_dict()
            })
    df_flat_sense_check = pd.DataFrame(flat_sense_check)
    df_flat_sense_check.to_csv(get_processed_path("dq_value_sense_check.csv"), index=False)
