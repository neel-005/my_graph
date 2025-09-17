import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Title
st.title("Iris Data Graph with Statistics")

# Load data
df = pd.read_csv("Iris.csv", header=None)
df.columns = ["col1", "col2", "col3", "col4", "col5","col6"]

# Select numeric columns
numeric_df = df[["col1", "col2", "col3", "col4","col5"]]

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
st.subheader("Statistics Table")
st.dataframe(stats)

# --- LINE PLOT of original data ---
st.subheader("Graph of Data with Average Stats Lines")
fig, ax = plt.subplots(figsize=(10, 5))

numeric_df.plot(ax=ax)

ax.set_title("Graph of original data with the line of avg stats data")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid(True, linestyle="--", alpha=0.6)

# Add horizontal lines for average stats
colors = ["red", "green", "blue", "orange", "purple", "brown", "skyblue", "#303F9F"]

for i, stat in enumerate(stats.columns):
    avg_value = stats[stat].mean()
    ax.axhline(y=avg_value, color=colors[i], linestyle="--", linewidth=1.5,
               label=f"Avg {stat}")

ax.legend()

st.pyplot(fig)

