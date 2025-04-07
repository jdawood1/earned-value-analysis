# Homework: Earned Value Analysis
# Task: EVA Metric Calculations
#
# Description:
# This script connects to the SQLite database EVA_data.db, reads PV, AC, and EV values,
# computes standard Earned Value Analysis metrics, and exports the results to EVA_Analysis.csv.
# It calculates CV, SV, CPI, SPI, and TCPI for each Module/Task/Week entry.

import sqlite3
import pandas as pd
import numpy as np

# --- Step 1: Connect to the SQLite database ---
db_path = "EVA_data.db"
conn = sqlite3.connect(db_path)

# --- Step 2: Load PV, AC, EV tables into pandas DataFrames ---
pv_df = pd.read_sql_query("SELECT * FROM PV", conn)
ac_df = pd.read_sql_query("SELECT * FROM AC", conn)
ev_df = pd.read_sql_query("SELECT * FROM EV", conn)

# --- Step 3: Merge tables on Module, Task, and Week ---
merged_df = pd.merge(pv_df, ac_df, on=["Module", "Task", "Week"], how="outer")
merged_df = pd.merge(merged_df, ev_df, on=["Module", "Task", "Week"], how="outer")

# Fill missing values with 0 (in case some weeks are missing)
merged_df.fillna(0, inplace=True)

# --- Step 4: Compute BAC per task (PV at week 7) ---
# BAC is used to calculate TCPI (To-Complete Performance Index)
bac_df = pv_df[pv_df["Week"] == 7].groupby(["Module", "Task"])["PV"].sum().reset_index()
bac_df.rename(columns={"PV": "BAC"}, inplace=True)

# Merge BAC into main dataframe
merged_df = pd.merge(merged_df, bac_df, on=["Module", "Task"], how="left")

# --- Step 5: Calculate EVA metrics ---
merged_df["CV"] = merged_df["EV"] - merged_df["AC"]            # Cost Variance
merged_df["SV"] = merged_df["EV"] - merged_df["PV"]            # Schedule Variance
merged_df["CPI"] = np.where(merged_df["AC"] != 0, merged_df["EV"] / merged_df["AC"], np.nan)
merged_df["SPI"] = np.where(merged_df["PV"] != 0, merged_df["EV"] / merged_df["PV"], np.nan)
merged_df["TCPI"] = np.where(
    (merged_df["BAC"] - merged_df["AC"]) != 0,
    (merged_df["BAC"] - merged_df["EV"]) / (merged_df["BAC"] - merged_df["AC"]),
    np.nan
)

# --- Step 6: Round metrics for clearer presentation ---
merged_df = merged_df.round({
    "PV": 2, "AC": 2, "EV": 2,
    "CV": 2, "SV": 2, "CPI": 2, "SPI": 2, "TCPI": 2
})

# --- Step 7: Export to CSV ---
output_file = "EVA_Analysis.csv"
merged_df.to_csv(output_file, index=False)
conn.close()

print(f"\u2705 EVA metrics calculated and saved to {output_file}")

