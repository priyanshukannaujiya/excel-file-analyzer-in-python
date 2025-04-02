# Excel & CSV Data Analysis Tool

This Streamlit application provides a user-friendly interface for basic data analysis of Excel (.xlsx, .xls) and CSV files. Simply upload your data and explore its key characteristics.

## Features

* **File Upload:** Easily upload your Excel or CSV files.
* **Dataset Summary:** View the total number of rows and columns in your dataset.
* **Column Information:** Get a detailed overview of each column, including:
    * Column Name
    * Data Type
    * Number of Missing Values
* **Basic Statistics:** Display descriptive statistics (count, mean, standard deviation, min, max, quartiles) for numerical columns.
* **Duplicate Value Detection:** Identify and display duplicate rows within your dataset.
* **Correlation Matrix:** Visualize the correlation between numerical columns using a heatmap.
* **Data Filtering:** Filter your data based on unique values in a selected column.
* **Data Visualization:** Generate histograms and boxplots for selected numerical columns to understand their distribution.

## How to Use

1.  **Upload File:** Click on the "Browse files" button and select your Excel (.xlsx, .xls) or CSV file.
2.  **Explore Summary:** Once the file is uploaded, the application will automatically display a summary of your dataset, including the number of rows and columns.
3.  **View Column Information:** Scroll down to see detailed information about each column, such as its data type and the count of missing values.
4.  **Examine Basic Statistics:** For numerical columns, you'll find a table with basic statistical measures.
5.  **Check for Duplicates:** The application will report the total number of duplicate rows and display them in a table if any are found.
6.  **Analyze Correlations:** If your data contains numerical columns, a correlation matrix heatmap will be displayed, showing the relationships between these columns.
7.  **Filter Data:**
    * Select a column from the "Select a column to filter:" dropdown.
    * Choose a specific value from the "Select a value:" dropdown to filter the data.
    * The filtered data will be displayed below.
8.  **Visualize Data:**
    * Select a numerical column from the "Select a numerical column:" dropdown.
    * A histogram (showing the distribution) and a boxplot (summarizing the distribution and identifying potential outliers) for the selected column will be displayed.

## Libraries Used

* **pandas:** For data manipulation and analysis.
* **streamlit:** For creating the interactive web application.
* **matplotlib.pyplot:** For basic plotting.
* **seaborn:** For enhanced data visualization, particularly the heatmap and statistical plots.

## Getting Started (for running locally)

1.  **Install Python:** Make sure you have Python installed on your system.
2.  **Install Libraries:** Open your terminal or command prompt and run the following command to install the necessary libraries:
    ```bash
    pip install pandas streamlit matplotlib seaborn openpyxl
    ```
    *(Note: `openpyxl` is required for reading Excel files)*
3.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `data_analyzer.py`).
4.  **Run the Application:** Navigate to the directory where you saved the file in your terminal or command prompt and run the Streamlit application using the command:
    ```bash
    streamlit run data_analyzer.py
    ```
5.  **Open in Browser:** Streamlit will automatically open a new tab in your web browser where you can interact with the data analysis tool.

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please feel free to open an issue or submit a pull request on the (hypothetical) repository.
