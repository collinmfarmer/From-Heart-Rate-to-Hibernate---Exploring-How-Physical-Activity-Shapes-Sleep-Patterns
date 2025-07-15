# Importing packages 
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

Tk().withdraw()  # Hide the root window
filename = askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
df = pd.read_csv(filename)

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

# Create output filename by adding "cleaned" before the extension
base, ext = os.path.splitext(filename)
output_filename = f"{base}_cleaned{ext}"

daily_filled.to_csv(output_filename, index=False)