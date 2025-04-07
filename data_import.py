# Homework: Earned Value Analysis
# Task: Data Import and Preparation
#
# Description:
# This script imports PV, AC, and EV project data from CSV files, cleans and reshapes the data,
# and stores them into an SQLite database named EVA_data.db. Each data type is stored in its own
# table (PV, AC, EV). The script handles all potential formatting inconsistencies and prepares
# the data for analysis.

import pandas as pd
import sqlite3
import os

# Define file paths for source data and target database
pv_file = "PV_data.csv"
ac_file = "AC_data.csv"
ev_file = "EV_data.csv"
db_file = "EVA_data.db"

# --- Helper function to clean and reshape data ---
def reshape_and_clean(df, value_name):
    """
    Transforms raw cumulative project data into a clean long-format DataFrame.

    Parameters:
        df (pd.DataFrame): Raw input DataFrame from CSV.
        value_name (str): The value label (e.g., 'PV', 'AC', or 'EV').

    Returns:
        pd.DataFrame: Cleaned and reshaped DataFrame with columns: Module, Task, Week, value_name.
    """
    weeks = df.iloc[0, 1:].values
    task_names = df.iloc[1:, 0].ffill()  # Fill forward merged cells
    df_cleaned = df.iloc[1:, 1:].copy()
    df_cleaned.columns = weeks

    df_cleaned.insert(0, "Task", task_names)
    df_melted = df_cleaned.melt(id_vars=["Task"], var_name="Week", value_name=value_name)

    df_melted["Module"] = df_melted["Task"].str.extract(r"(Module [A-Z])")
    df_melted["Task"] = df_melted["Task"].str.extract(r"(Task \d+)")

    df_melted[value_name] = df_melted[value_name].replace('[\\$,]', '', regex=True)
    df_melted[value_name] = pd.to_numeric(df_melted[value_name], errors='coerce')

    df_melted.dropna(subset=["Week", value_name], inplace=True)
    df_melted["Week"] = pd.to_numeric(df_melted["Week"], errors='coerce').astype("Int64")

    return df_melted[["Module", "Task", "Week", value_name]]

# --- Load raw CSV data ---
pv_df_raw = pd.read_csv(pv_file)
ac_df_raw = pd.read_csv(ac_file)
ev_df_raw = pd.read_csv(ev_file)

# --- Clean and reshape data ---
pv_clean = reshape_and_clean(pv_df_raw, "PV")
ac_clean = reshape_and_clean(ac_df_raw, "AC")
ev_clean = reshape_and_clean(ev_df_raw, "EV")

# --- Create or replace the SQLite database ---
if os.path.exists(db_file):
    os.remove(db_file)  # Delete an existing database for a clean import

conn = sqlite3.connect(db_file)

# Write each cleaned dataset to its own table
pv_clean.to_sql("PV", conn, index=False)
ac_clean.to_sql("AC", conn, index=False)
ev_clean.to_sql("EV", conn, index=False)

conn.close()

print("\u2705 Data import complete. Tables 'PV', 'AC', and 'EV' created in EVA_data.db.")

