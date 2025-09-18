import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# ----------------- Title -----------------
st.title("Iris Dataset Statistics & Graphs")

# ----------------- File Upload -----------------
uploaded_file = st.file_uploader("Upload your Iris CSV file", type="csv")

# ----------------- Load Data -----------------
if uploaded_file:
    df = pd.read_csv(uploaded_file, header=None)
    st.success("File uploaded successfully!")
elif os.path.exists("iris.csv"):
    df = pd.read_csv("iris.csv", header=None)
    st.info("Loaded iris.csv from GitHub repo")
else:
    df = sns.load_dataset("iris")
    st.warning("iris.csv not found in repo. Using Seaborn's default Iris dataset.")

# ----------------- Column Naming -----------------
if "species" not in df.columns:
    df.columns = ["col1", "col2", "col3", "col4", "col5"]

# ----------------- Select Numeric Columns -----------------
numeric_df = df.select_dtypes(include='number')

# ----------------- Statistics Calculation -----------------
mean_vals = numeric_df.mean()
median_vals = numeric_df.median()
mode_vals = numeric_df.mode().iloc[0]
std_vals = numeric_df.std()
var_vals = numeric_df.var()
min_vals = numeric_df.min()
max_vals = numeric_df.max()
range_vals = max_vals - min_vals

# Combine stats into a DataFrame
stats = pd.DataFrame({
    "Mean": mean_vals,
    "Median": median_vals,
    "Mode": mode_vals,
    "Std Dev": std_vals,
    "Variance": var_vals,
    "Min": min_vals,
    "Max": max_vals,
    "Range": range_vals
})

# ----------------- Display Stats -----------------
st.subheader("Statistics Table")
st.dataframe(stats)

# ----------------- Select Stats to Plot -----------------
selected_stats = st.multiselect("Select statistics lines to display on graph", stats.columns, default=stats.columns)

# ----------------- Plot Graph -----------------
st.subheader("Graph of Data with Selected Statistics Lines")
fig, ax = plt.subplots(figsize=(10, 5))

numeric_df.plot(ax=ax, linewidth=2)

# Color palette for stats lines
colors = plt.cm.tab10.colors

for i, stat in enumerate(selected_stats):
    avg_value = stats[stat].mean()
    ax.axhline(y=avg_value, color=colors[i % 10], linestyle="--", linewidth=1.5, label=f"Avg {stat}")

ax.set_title("Iris Data with Statistics Lines")
ax.set_xlabel("Index")
ax.set_ylabel("Values")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

st.pyplot(fig)
