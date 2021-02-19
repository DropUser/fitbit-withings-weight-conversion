import pandas as pd
import glob

# These variables should be edited to reflect your OS and data location.
source_folder = "D:\\Weight\\"
output_folder = "D:\\Weight\\output\\"

# Read all files and combine into single dataframe
all_files = glob.glob(source_folder + "*weight*.json")
df = pd.concat((pd.read_json(f, convert_dates=False) for f in all_files))

# Fix date into datetime
df["date"] = pd.to_datetime(df["date"] + " " + df["time"])

# Select only required columns and sort/fix index
df = df[["date", "weight", "fat"]]
df.sort_values("date", inplace=True)
df.reset_index(drop=True, inplace=True)

# Set chunk size and create seperate CSV file for each.
chunk_size = 299
for filenum, position in enumerate(range(0, df.shape[0], chunk_size)):
    sub_df = df.iloc[position:position + chunk_size]
    sub_df.to_csv(f"{output_folder}weight_output_{filenum}.csv", index=False)
