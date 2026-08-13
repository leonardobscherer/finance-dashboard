import pandas as pd
import streamlit as st

def upload_csv_files():
    files = st.file_uploader('Select CSV files',
                             type='csv',
                             accept_multiple_files=True
                             )

    if not files:
        return None
   
        
    return files

