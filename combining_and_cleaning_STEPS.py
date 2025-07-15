# Importing packages
import pandas as pd
import glob
import os

# Using glob to read in all the steps CSVs
data_files = r".\Raw CSVs"
df= pd.DataFrame()
file_list = glob.glob(os.path.join(data_files, "steps_2025*.csv")) 

# Checking to confirm the file path and pattern of the files are correct
if file_list:
    df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
else:
    print("No matching CSV files found. Check your path and pattern.")

# Convert "timestamp" to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Set "timestamp" as index
df.set_index("timestamp", inplace=True)

# Group by day and sum "steps"
daily = df["steps"].resample("D").sum()

# Fill missing days with zero
daily_filled = daily.fillna(0)

# Reset index to have "timestamp" as a column again
daily_filled = daily_filled.reset_index()

# Remove time from "timestamp"
daily_filled["timestamp"] = daily_filled["timestamp"].dt.date

# Rename columns
daily_filled = daily_filled.rename(columns={"steps": "total_steps_taken"})
daily_filled = daily_filled.rename(columns={"timestamp": "date"})

# Create new cleaned CSV for the steps data
daily_filled.to_csv("cleaned_daily_steps.csv", index=False) 