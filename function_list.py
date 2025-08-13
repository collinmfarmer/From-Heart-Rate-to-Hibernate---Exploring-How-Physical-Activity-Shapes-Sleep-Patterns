import pandas as pd
import glob
import os



def pull_csv_concat(csv_name: str):
    """
    Searches for CSV files matching the given pattern in the Raw CSVs folder, reads them in, and concatenates them into a single dataframe

    Parameters:
    - csv_name (str): Filename pattern

    Returns: 
    - Dataframe made from all concatenated files matching the filename pattern
    """
    data_files = r".\Raw CSVs"
    df= pd.DataFrame()
    file_list = glob.glob(os.path.join(data_files, csv_name)) 

    if file_list:
        df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
    else:
        print("No matching CSV files found. Check your path and pattern.")

    return df





def write_dfs_to_sql(df_dict, conn, if_exists = "replace"):
    """
    Write multiple dataframes to SQL database

    Parameters:
    - df_dict: dictionary where keys are table names and values are dataframes
    - conn: SQL connection
    - if_exists: how to behave if the table already exists

    """
    for table_name, df in df_dict.items():
        df.to_sql(table_name, conn, if_exists = if_exists, index=False)





def resample_daily(df, time_col, value_col, agg_method="sum", fill_missing=True):
    """
    Resamples a DataFrame to daily frequency

    Parameters:
    - df (pd.DataFrame): Input DataFrame
    - time_col (str): Name of the date column
    - value_col (str): Name of the value column to aggregate
    - agg_method (str): Aggregation method (sum or mean)
    - fill_missing (bool): Whether to fill missing days with 0

    Returns:
    - pd.DataFrame: Daily resampled DataFrame with date and aggregated values
    """
    # Convert date column to datetime
    df[time_col] = pd.to_datetime(df[time_col])

    # Set date as index
    df = df.set_index(time_col)

    # Resample by day using specified aggregation
    if agg_method == "sum":
        daily = df[value_col].resample("D").sum()
    elif agg_method == "mean":
        daily = df[value_col].resample("D").mean()
    else:
        raise ValueError("agg_method must be sum or mean")

    # Fill missing days with 0 if requested
    if fill_missing:
        daily = daily.fillna(0)

    # Reset index to restore date column
    daily_filled = daily.reset_index()

    return daily_filled