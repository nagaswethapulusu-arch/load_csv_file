import pandas as pd
import streamlit as st

st.set_page_config(page_title="Load a CSV Dataset", page_icon="📂", layout="wide")
st.title("📂 Load a CSV Dataset with Pandas")
st.caption("Upload a CSV file, or use the sample Student Performance dataset, to view its first and last records.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])

try:
    df = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("student_performance.csv")
    st.success("Dataset loaded successfully!")
except Exception as e:
    st.error(f"Could not load the dataset: {e}")
    st.stop()

n = st.slider("Number of records to show", 1, 20, 5)

c1, c2, c3 = st.columns(3)
c1.metric("Rows", df.shape[0])
c2.metric("Columns", df.shape[1])
c3.metric("Missing values", int(df.isnull().sum().sum()))

st.subheader(f"First {n} records (head)")
st.dataframe(df.head(n), use_container_width=True)

st.subheader(f"Last {n} records (tail)")
st.dataframe(df.tail(n), use_container_width=True)

with st.expander("Column info and summary statistics"):
    st.write(pd.DataFrame({"dtype": df.dtypes.astype(str), "missing": df.isnull().sum()}))
    st.write(df.describe())
