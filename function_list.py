import pandas as pd
import glob
import os



# Creating a function to read in and concat all the CSVs using a filepath
def pull_csv_concat(csv_name: str):
    """
    Function:
    Searches for CSV files matching the given pattern in the Raw CSVs folder, reads them in, and concatenates them into a single dataframe.

    Parameters:
    csv_name (str): Filename pattern

    Returns: 
    Dataframe made from all concatenated files matching the filename pattern. 

    """
    data_files = r".\Raw CSVs"
    df= pd.DataFrame()
    file_list = glob.glob(os.path.join(data_files, csv_name)) 

    if file_list:
        df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
    else:
        print("No matching CSV files found. Check your path and pattern.")

    return df





# Creating a function to 
def write_dfs_to_sql(df_dict, conn, if_exists = "replace"):
    """
    Function:
    Write multiple dataframes to SQL database. 

    Parameters:
    df_dict: dictionary where keys are table names and values are dataframes
    conn: SQL connection
    if_exists: how to behave if the table already exists

    """
    for table_name, df in df_dict.items():
        df.to_sql(table_name, conn, if_exists = if_exists, index=False)




# 
