# Importing packages
import pandas as pd
import glob
import os
from function_list import pull_csv_concat
from function_list import resample_daily

# Using pull_csv_concat function to read in all the steps CSVs and combine them
df = pull_csv_concat("steps_*.csv")

# Resampled Dataframe to daily frequency 
daily_filled = resample_daily(df, time_col="timestamp", value_col="steps", agg_method="sum")

# Remove time from "timestamp"
daily_filled["timestamp"] = daily_filled["timestamp"].dt.date

# Rename columns
daily_filled = daily_filled.rename(columns={"steps": "total_steps_taken"})
daily_filled = daily_filled.rename(columns={"timestamp": "date"})

# Create new cleaned CSV for the steps data
daily_filled.to_csv("cleaned_daily_steps.csv", index=False) 