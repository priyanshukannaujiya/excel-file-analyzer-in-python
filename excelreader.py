import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext

class ExcelSummaryTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Data Summary Tool")
        
        # Create load button
        self.load_button = ttk.Button(self.root, text="Load Excel File", command=self.load_file)
        self.load_button.pack(pady=10)
        
        # Create output area
        self.output_area = scrolledtext.ScrolledText(self.root, width=100, height=25, wrap=tk.WORD)
        self.output_area.pack(padx=10, pady=10)
    
    def load_file(self):
        # Open file dialog to select Excel file
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=(("Excel Files", "*.xlsx *.xls"), ("All Files", "*.*"))
        )
        if file_path:
            try:
                # Read the Excel file
                data = pd.read_excel(file_path)
                summary = self.generate_summary(data)
                self.output_area.delete(1.0, tk.END)  # Clear previous output
                self.output_area.insert(tk.END, summary)
            except Exception as e:
                self.output_area.delete(1.0, tk.END)
                self.output_area.insert(tk.END, f"Error loading file: {e}")
    
    def generate_summary(self, data):
        # Generate a summary of the dataset
        summary = []
        summary.append("Summary of the Excel File:\n")
        summary.append(f"Number of Rows: {data.shape[0]}")
        summary.append(f"Number of Columns: {data.shape[1]}")
        summary.append("\nColumn Information:\n")
        
        for col in data.columns:
            summary.append(f" - {col}: {data[col].dtype}, Missing Values: {data[col].isnull().sum()}")
        
        summary.append("\nBasic Statistics for Numerical Columns:\n")
        summary.append(data.describe().to_string())
        
        return "\n".join(summary)

if __name__ == "__main__":
    root = tk.Tk()
    tool = ExcelSummaryTool(root)
    root.mainloop()
