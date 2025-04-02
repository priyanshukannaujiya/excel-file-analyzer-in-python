import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit UI Setup
st.title("Excel & CSV Data Analysis Tool")

# File Upload
uploaded_file = st.file_uploader("Upload an Excel or CSV file", type=["xlsx", "xls", "csv"])

if uploaded_file:
    try:
        # Read the uploaded file (CSV or Excel)
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        else:
            data = pd.read_excel(uploaded_file)
        
        # Display dataset summary
        st.write("### Summary of the File:")
        st.write(f"**Number of Rows:** {data.shape[0]}")
        st.write(f"**Number of Columns:** {data.shape[1]}")
        
        # Column Information
        st.write("### Column Information:")
        column_info = {
            "Column Name": data.columns,
            "Data Type": [data[col].dtype for col in data.columns],
            "Missing Values": [data[col].isnull().sum() for col in data.columns]
        }
        st.dataframe(pd.DataFrame(column_info))
        
        # Display Basic Statistics for Numerical Columns
        st.write("### Basic Statistics for Numerical Columns:")
        st.dataframe(data.describe())
        
        # Detect Duplicate Values
        st.write("### Duplicate Values:")
        duplicate_rows = data[data.duplicated()]
        st.write(f"Total Duplicates: {duplicate_rows.shape[0]}")
        if not duplicate_rows.empty:
            st.dataframe(duplicate_rows)
        
        # Correlation Matrix
        st.write("### Correlation Matrix:")
        numeric_data = data.select_dtypes(include=['number'])
        if not numeric_data.empty:
            fig, ax = plt.subplots()
            sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
        else:
            st.write("No numerical columns found for correlation analysis.")
        
        # Data Filtering Options
        st.write("### Filter Data:")
        selected_column = st.selectbox("Select a column to filter:", data.columns)
        unique_values = data[selected_column].unique()
        selected_value = st.selectbox("Select a value:", unique_values)
        filtered_data = data[data[selected_column] == selected_value]
        st.write(f"Filtered Data (Where {selected_column} = {selected_value}):")
        st.dataframe(filtered_data)
        
        # Data Visualization (Histograms & Boxplots)
        st.write("### Data Visualization:")
        selected_numeric_column = st.selectbox("Select a numerical column:", numeric_data.columns)
        
        if selected_numeric_column:
            fig, ax = plt.subplots(1, 2, figsize=(12, 5))
            
            # Histogram
            sns.histplot(data[selected_numeric_column], bins=20, kde=True, ax=ax[0])
            ax[0].set_title(f"Histogram of {selected_numeric_column}")
            
            # Boxplot
            sns.boxplot(y=data[selected_numeric_column], ax=ax[1])
            ax[1].set_title(f"Boxplot of {selected_numeric_column}")
            
            st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error loading file: {e}")

