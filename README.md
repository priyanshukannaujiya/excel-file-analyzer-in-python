# Excel and CSV Data Analyzer in Python

A **Streamlit-based Excel and CSV data analysis tool** for quickly exploring datasets, checking data quality, calculating descriptive statistics, filtering records, and visualizing numerical columns.

## Overview

The application provides an interactive interface for exploratory data analysis (EDA) without requiring users to write pandas code for every dataset. Upload an Excel workbook or CSV file and inspect its structure, quality, distributions, and relationships.

## Features

- **Excel and CSV upload:** Work with `.xlsx`, `.xls`, and `.csv` datasets.
- **Dataset overview:** View the number of rows and columns.
- **Column profiling:** Inspect column names, data types, and missing-value counts.
- **Descriptive statistics:** Calculate count, mean, standard deviation, minimum, maximum, and quartiles for numerical columns.
- **Duplicate detection:** Identify duplicate records.
- **Correlation analysis:** Explore relationships between numerical variables with a correlation heatmap.
- **Interactive filtering:** Filter records using distinct values in a selected column.
- **Data visualization:** Generate histograms and box plots to understand distributions and potential outliers.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| pandas | Data loading and manipulation |
| Matplotlib | Data visualization |
| Seaborn | Statistical plots and heatmaps |
| openpyxl | Excel workbook support |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/priyanshukannaujiya/excel-file-analyzer-in-python.git
cd excel-file-analyzer-in-python
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install pandas streamlit matplotlib seaborn openpyxl
```

### 4. Launch the Streamlit application

Run the Python entry-point file in this repository:

```bash
streamlit run <application-file>.py
```

Replace `<application-file>.py` with the actual Streamlit script filename.

## Example Workflow

1. Upload an Excel or CSV dataset.
2. Review the dataset dimensions and column profile.
3. Check missing values and duplicate records.
4. Review descriptive statistics and the correlation heatmap.
5. Filter records and inspect histograms or box plots.

## Relevant Keywords

Python data analysis, Excel analyzer, CSV analyzer, Streamlit dashboard, pandas, exploratory data analysis, data cleaning, data profiling, data visualization, correlation heatmap.

## Author

[Priyanshu Kannaujiya](https://github.com/priyanshukannaujiya)

## Repository

https://github.com/priyanshukannaujiya/excel-file-analyzer-in-python
