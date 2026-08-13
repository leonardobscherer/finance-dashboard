import pandas as pd
from validation import validate_header,validate_values
from pathlib import Path


def load_csv(files):   
   
    
    dataframes = []

    for file in files:
        current_df = pd.read_csv(file)
        filename = file.name
        missing_headers = validate_header(current_df.columns.tolist())
        if missing_headers:
                print(f'The following column(s) is/are missing:{missing_headers} in {filename}')       
                return None
        validate_values(current_df)
        dataframes.append(current_df)
    df = pd.concat(dataframes, ignore_index=True) 
    return df
    

      
        






