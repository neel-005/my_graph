import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Title
st.title("📊 Iris Data Graph with Statistics")

# Load data
try:
    df = pd.read_csv("Iris.csv", header=None)
except FileNotFoundError:
    st.error("❌ 'iris.csv' not found. Please make sure it's uploaded to your GitHub repo.")
    st.stop()

# Preview raw data
st.subheader("🔍 Raw Data Preview")
st.dataframe(df.head())

# Assign column names based on actual structure
if df.shape[1] == 6:
    df.columns = ["col1", "col2", "col3", "col4", "col5", "col6"]
elif df.shape[1] == 5:
    df.columns = ["col1", "col2", "col3", "col4", "col5"]
else:
    st.error(f"Unexpected number of columns: {df.shape[1]}")
    st.stop()

# Select numeric columns and ensure clean conversion
numeric_df = df[["col1", "col2", "col3", "col4"]].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values (optional)
numeric_df = numeric_df.dropna()

# Calculate statistics
mean_vals = numeric_df.mean()
median_vals = numeric_df.median()
mode_vals = numeric_df.mode().iloc[0]
std_vals = numeric_df.std()
var_vals = numeric_df.var()
min_vals = numeric_df.min()
max_vals = numeric_df.max()
range_vals = max_vals - min_vals

# Put stats into DataFrame
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

# Show statistics table
st.subheader("📋 Statistics Table")
st.dataframe(stats)

# --- LINE PLOT of original data ---
st.subheader("📈 Graph of Data with Average Stats Lines")
fig, ax = plt.subplots(figsize=(10, 5))

numeric_df.plot(ax=ax)

ax.set_title("Graph of Original Data with Average Statistic Lines")
ax.set_xlabel("Sample Index")
ax.set_ylabel("Measurement Value")
ax.grid(True, linestyle="--", alpha=0.6)

# Add horizontal lines for average stats
colors = ["red", "green", "blue", "orange", "purple", "brown", "skyblue", "#303F9F"]

for i, stat in enumerate(stats.columns):
    avg_value = stats[stat].mean()
    ax.axhline(y=avg_value, color=colors[i % len(colors)], linestyle="--", linewidth=1.5,
               label=f"Avg {stat}")

ax.legend(loc="upper right")
st.pyplot(fig)

