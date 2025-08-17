import streamlit as st
import pandas as pd

def render_data_dashboard(df):
    st.subheader("Automated Data Dashboard")
    
    # Show numeric statistics
    st.write("**Descriptive statistics:**")
    st.write(df.describe())

    # Top categories for first categorical column
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        col = cat_cols[0]
        st.write(f"**Top categories in {col}:**")
        st.bar_chart(df[col].value_counts().head(10))

    # Distribution of first numeric column
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        col = num_cols
        st.write(f"**Distribution of {col}:**")
        st.line_chart(df[col].head(100))
