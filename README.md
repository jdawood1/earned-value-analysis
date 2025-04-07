# Earned Value Analysis (EVA) – Project Guide

This project implements a complete workflow for conducting Earned Value Analysis (EVA) on a multi-module project spanning seven weeks. It uses Python to process cumulative cost and value data, calculate industry-standard EVA metrics, and produce a final report.

---

## 📁 Project Structure

```
├── data_import.py           # Loads and stores cleaned data in SQLite
├── eva_calculations.py      # Performs EVA metric calculations
├── analysis.md              # Detailed data-driven interpretation
├── EVA_data.db              # SQLite DB (auto-generated)
├── EVA_Analysis.csv         # Metric output file (auto-generated)
├── PV_data.csv              # Planned Value data (input)
├── AC_data.csv              # Actual Cost data (input)
├── EV_data.csv              # Earned Value data (input)
├── .gitignore               # Ignores virtual env, DB, output files
└── README.md                # This file
```

---

## 🚀 How to Run the Project

### 1. Set Up Environment
```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
pip install pandas numpy matplotlib
```

### 2. Import and Clean Data
```bash
python data_import.py
```
This will:
- Load `PV_data.csv`, `AC_data.csv`, `EV_data.csv`
- Clean and reshape the data
- Store into `EVA_data.db` with `PV`, `AC`, and `EV` tables

### 3. Perform EVA Calculations
```bash
python eva_calculations.py
```
This will:
- Load data from the database
- Calculate CV, SV, CPI, SPI, and TCPI
- Export results to `EVA_Analysis.csv`

### 4. Read the Analysis
Open `analysis.md` to review interpretation of the metrics.

---

## 🧪 Key Metrics Calculated

- **CV**: Cost Variance
- **SV**: Schedule Variance
- **CPI**: Cost Performance Index
- **SPI**: Schedule Performance Index
- **TCPI**: To-Complete Performance Index

Each metric is calculated per Module, Task, and Week.

---

## 📌 Notes
- All calculations are programmatic.
- No manual entry or hardcoded values are used.
- Outputs are reproducible and driven by the original data files.

---

## 👨‍💻 Author
Developed by John Dawood for academic purposes. Project demonstrates Python scripting, SQLite integration, and data-driven analysis using real-world project management metrics.
