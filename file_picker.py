import tkinter as tk
from tkinter import filedialog
import pandas as pd
import streamlit as st

def pick_csv_files():
    root = tk.Tk()
    root.withdraw()
    paths = filedialog.askopenfilenames(title = 'Select one or multiple files', filetypes=[('CSV files', '*.csv')])
    root.destroy()
    dataframes=[]

    for path in paths:
        df = pd.read_csv(path)
        dataframes.append(df)
    if not paths:
        return None
    return paths

def upload_csv_files():
    files = st.file_uploader('Select CSV files',
                             type='csv',
                             accept_multiple_files=True
                             )

    if not files:
        return None
   
        
    return files

