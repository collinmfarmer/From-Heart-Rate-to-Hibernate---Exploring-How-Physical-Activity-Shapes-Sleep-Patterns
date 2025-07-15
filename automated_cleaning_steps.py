# Importing packages 
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw()  # Hide the root window
filename = askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
df = pd.read_csv(filename)

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

# Create output filename by adding "cleaned" before the extension
base, ext = os.path.splitext(filename)
output_filename = f"{base}_cleaned{ext}"

daily_filled.to_csv(output_filename, index=False)