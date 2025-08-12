# Importing packages
import pandas as pd
import glob
import os
from function_list import pull_csv_concat

# Using pull_csv_concat function to read in all the active zone minutes CSVs and combine them
df = pull_csv_concat("Active Zone Minutes -*.csv")

# Convert "date_time" to datetime
df["date_time"] = pd.to_datetime(df["date_time"])

# Set "date_time" as index
df.set_index("date_time", inplace=True)

# Group by day and sum "total_minutes"
daily = df["total_minutes"].resample("D").sum()

# Fill missing days with zero
daily_filled = daily.fillna(0)

# Reset index to have "date_time" as a column again
daily_filled = daily_filled.reset_index()

# Rename columns
daily_filled = daily_filled.rename(columns={"total_minutes": "active_zone_minutes"})
daily_filled = daily_filled.rename(columns={"date_time": "date"})

# Create new cleaned CSV for the daily active zone minutes
daily_filled.to_csv("cleaned_daily_active_zone_minutes.csv", index=False) 