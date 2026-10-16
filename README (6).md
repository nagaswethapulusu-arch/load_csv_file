# 📂 Load a CSV Dataset with Pandas

Load a CSV dataset using Pandas and display its first and last records. A first step in any machine learning workflow: importing real-world tabular data.

## Objective
Learn how to import real-world tabular data for machine learning workflows.

## Tools
- Python
- Pandas
- Jupyter Notebook
- Streamlit (for the deployed demo)

## Dataset
`student_performance.csv` is a sample Student Performance dataset (50 rows, 7 columns):
`student_id, gender, hours_studied, attendance_pct, previous_score, final_score, result`

## Project Structure
```
├── Load_CSV_Dataset.ipynb     # Main notebook
├── student_performance.csv    # Dataset
├── app.py                     # Streamlit web app
├── requirements.txt           # Dependencies
└── README.md
```

## What the Notebook Does
1. Imports Pandas
2. Loads the CSV with `pd.read_csv()`
3. Shows the first five records with `head()`
4. Shows the last five records with `tail()`
5. Checks the load: shape, columns, missing values, `info()` and `describe()`

## Run Locally
```bash
git clone https://github.com/<your-username>/load-csv-dataset-pandas.git
cd load-csv-dataset-pandas
pip install -r requirements.txt

jupyter notebook Load_CSV_Dataset.ipynb   # notebook
streamlit run app.py                      # web app
```

## Deploy (Streamlit Community Cloud)
1. Push this repo to GitHub (include `student_performance.csv`).
2. Go to share.streamlit.io and click **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. Click **Deploy**.

## Interview Questions
- **What is a CSV file?** A plain-text file where values are separated by commas, with one record per line.
- **How do you load a CSV with Pandas?** `df = pd.read_csv('file.csv')`
- **What is a DataFrame?** A 2-D labelled table of rows and columns, the main data structure in Pandas.

## Author
Swetha, AI & ML Track, Veda Technology
