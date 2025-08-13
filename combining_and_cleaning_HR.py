# Importing packages
import pandas as pd
import glob
import os
from function_list import pull_csv_concat
from function_list import resample_daily

# Using pull_csv_concat function to read in all the heart rate CSVs and combine them
df = pull_csv_concat("heart_rate_*.csv")

# Resampled Dataframe to daily frequency 
daily_filled = resample_daily(df, time_col="timestamp", value_col="beats per minute", agg_method="mean")

# Remove time from "timestamp"
daily_filled["timestamp"] = daily_filled["timestamp"].dt.date

# Renamed columns
daily_filled = daily_filled.rename(columns={"beats per minute": "avg_beats_per_minute"})
daily_filled = daily_filled.rename(columns={"timestamp": "date"})

# Create new cleaned CSV for the daily average heart rate data
daily_filled.to_csv("cleaned_daily_heart_rate.csv", index=False) 