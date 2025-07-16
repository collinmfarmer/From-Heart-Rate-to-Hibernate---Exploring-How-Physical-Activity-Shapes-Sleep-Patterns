# Importing packages
import pandas as pd
import glob
import os
import json

# Using glob to read in all the sleep JSONs
file_paths = glob.glob(r".\Raw JSON\sleep-*.json")

combined_data = []

for file_path in file_paths:
    with open(file_path, 'r') as f:
        data = json.load(f)
        if isinstance(data, list):
            combined_data.extend(data)
        else:
            print("The JSON file is not formatted correctly for this program.")

# Save the combined data to a new JSON file
with open('combined_sleep.json', 'w') as outfile:
    json.dump(combined_data, outfile, indent=4)



# Reading in the new flattened JSON file
f = open("combined_sleep.json", "r")
file = json.loads(f.read())

# Converting flattened JSON file to CSV
df_flattened = pd.json_normalize(file)

# Create new CSV for the flattened sleep data
df_flattened.to_csv("combined_and_flattened_sleep.csv", index=False) 