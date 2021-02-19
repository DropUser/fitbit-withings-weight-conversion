import pandas as pd
import os
import glob


def convert_data(source_folder, output_folder):
    # Read all files and combine into single dataframe
    all_files = glob.glob(os.path.join(source_folder, "*weight*.json"))
    df = pd.concat((pd.read_json(f, convert_dates=False) for f in all_files))

    # Fix date into datetime
    df["date"] = pd.to_datetime(df["date"] + " " + df["time"])

    # Select only required columns and sort/fix index
    df = df[["date", "weight", "fat"]]
    df.sort_values("date", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Set chunk size and create separate CSV file for each.
    chunk_size = 299

    # Check if output folder exists, if not create it.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filenum, position in enumerate(range(0, df.shape[0], chunk_size)):
        sub_df = df.iloc[position:position + chunk_size]
        # Write output file
        sub_df.to_csv(os.path.join(output_folder, f"weight_output_{filenum}.csv"), index=False)


if __name__ == "__main__":
    # Get required parameters from the user
    source_folder = input("Enter Source Folder: ")
    output_folder = input("Enter Output Folder: ")
    convert_data(source_folder, output_folder)
