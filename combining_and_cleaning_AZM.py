# Importing packages
import pandas as pd
import glob
import os
from function_list import pull_csv_concat
from function_list import resample_daily

# Using pull_csv_concat function to read in all the active zone minutes CSVs and combine them
df = pull_csv_concat("Active Zone Minutes -*.csv")

# Resampled Dataframe to daily frequency 
daily_filled = resample_daily(df, time_col="date_time", value_col="total_minutes", agg_method="sum")

# Rename columns
daily_filled = daily_filled.rename(columns={"total_minutes": "active_zone_minutes"})
daily_filled = daily_filled.rename(columns={"date_time": "date"})

# Create new cleaned CSV for the daily active zone minutes
daily_filled.to_csv("cleaned_daily_active_zone_minutes.csv", index=False) 