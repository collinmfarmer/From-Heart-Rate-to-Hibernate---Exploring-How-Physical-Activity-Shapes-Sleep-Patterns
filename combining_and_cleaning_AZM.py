# Importing packages
import pandas as pd
import glob
import os

# Using glob to read in all the active zone minutes CSVs
data_files = r".\Raw CSVs"
df= pd.DataFrame()
file_list = glob.glob(os.path.join(data_files, "Active Zone Minutes - 2025*.csv")) 

# Checking to confirm the file path and pattern of the files are correct
if file_list:
    df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
else:
    print("No matching CSV files found. Check your path and pattern.")

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