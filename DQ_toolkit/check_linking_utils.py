import json
import pandas as pd
from itertools import combinations

PATIENT_ID_COLUMNS = [
    # List of all columns in all tables that contain patient ID fields
]

MISSING_VALUE_FILLERS = {
    # Dictionary where the keys are the names of the tables and the values are
    # a list of all characters that denote invalid values, e.g. '99'
}

INGESTION_FUNCTION = "ingestion_function"

ALL_TABLES = {
    # Nested dictionary where each entry is:
    # table_name: {INGESTION_FUNCTION: function to ingest table}
}


def get_unique_ids(df: pd.DataFrame) -> dict[set]:
    """
    Creates a dictionary where the keys are the different id columns
    and the values are the set of all values in the table

    Args:
        df (pd.DataFrame): table of event-level data

    Returns:
        dict[set]: dictionary of unique ids
    """
    unique_patient_ids = set()

    for column in PATIENT_ID_COLUMNS:
        if column in df.columns:
            unique_patient_ids.update(set(df[column].dropna().astype(str).unique()))
            if column in MISSING_VALUE_FILLERS.keys():
                unique_patient_ids.discard(set(MISSING_VALUE_FILLERS[column] + [""]))
            else:
                unique_patient_ids.discard("")

    return list(unique_patient_ids)


def check_all_tables():
    """
    Runs through all input tables and gathers all the unique ids in each
    table.
    """

    unique_patient_ids = {}

    for key, value in ALL_TABLES.items():
        df = value[INGESTION_FUNCTION]()
        unique_patient_ids[key] = get_unique_ids(df)

    with open(("dq_unique_ids.json"), "w") as fp:
        json.dump(unique_patient_ids, fp)


def check_linking():
    """
    Uses the lists of unique patient ids generated in 'check_table_completeness'
    to see how many linkages there are between each table.
    """
    with open("dq_unique_ids.json") as json_data:
        all_ids_dict = json.load(json_data)

    df_check_linking = pd.DataFrame()

    for table in ALL_TABLES.keys():
        df_check_linking.loc[table, table] = len(all_ids_dict[table])

    for table_1, table_2 in combinations(ALL_TABLES.keys(), 2):
        df_check_linking.loc[table_1, table_2] = df_check_linking.loc[
            table_2, table_1
        ] = len(set(all_ids_dict[table_1]).intersection(set(all_ids_dict[table_2])))

    df_check_linking_percentages = pd.DataFrame()

    for row in range(len(ALL_TABLES)):
        for column in range(len(ALL_TABLES)):
            if row == column:
                df_check_linking[row, column] = None
            elif row < column:
                df_check_linking[row, column] = (
                    df_check_linking[row, column] / df_check_linking[row, row]
                )
            elif column < row:
                df_check_linking[row, column] = (
                    df_check_linking[row, column] / df_check_linking[column, column]
                )

    df_check_linking.to_csv("dq_check_table_linking.csv")
    df_check_linking_percentages.to_csv("dq_check_table_linking_percentages.csv")
