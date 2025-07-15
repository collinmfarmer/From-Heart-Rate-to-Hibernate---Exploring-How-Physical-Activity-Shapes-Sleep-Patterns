# Importing packages
import pandas as pd
import glob
import os

# Using glob to read in all the heart rate CSVs
data_files = r".\Raw CSVs"
df= pd.DataFrame()
file_list = glob.glob(os.path.join(data_files, "heart_rate_2025*.csv")) 

# Checking to confirm the file path and pattern of the files are correct
if file_list:
    df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
else:
    print("No matching CSV files found. Check your path and pattern.")

# Convert "timestamp" to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Set "timestamp" as index
df.set_index("timestamp", inplace=True)

# Group by day and sum "beats per minute"
daily = df["beats per minute"].resample("D").mean()

# Fill missing days with zero
daily_filled = daily.fillna(0)

# Reset index to have "timestamp" as a column again
daily_filled = daily_filled.reset_index()

# Remove time from "timestamp"
daily_filled["timestamp"] = daily_filled["timestamp"].dt.date

# Renamed columns
daily_filled = daily_filled.rename(columns={"beats per minute": "avg_beats_per_minute"})
daily_filled = daily_filled.rename(columns={"timestamp": "date"})

# Create new cleaned CSV for the daily average heart rate data
daily_filled.to_csv("cleaned_daily_heart_rate.csv", index=False) 