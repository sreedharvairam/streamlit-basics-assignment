import streamlit as st
import pandas as pd

# Task 1: Build the App
st.title("Sales Summary Dashboard")
st.subheader("Interactive view of sales performance by category")

# Create hardcoded dataset
data = {
    "Product": ["Widget A", "Gadget B", "Widget C", "Tool D", "Gadget E", "Tool F"],
    "Category": ["Widgets", "Gadgets", "Widgets", "Tools", "Gadgets", "Tools"],
    "Sales": [1200, 2500, 800, 1500, 3100, 900]
}

df = pd.DataFrame(data)

# Task 2: Add a Sidebar
# Moving the selectbox filter to the sidebar
categories = df["Category"].unique()
selected_category = st.sidebar.selectbox("Select a Category", options=categories)

# Filter the DataFrame based on selection
filtered_df = df[df["Category"] == selected_category]

# Display results in the main content area
st.write(f"### Showing data for: {selected_category}")
st.dataframe(filtered_df)

# Line chart of Sales values for the selected category
st.line_chart(filtered_df.set_index("Product")["Sales"])