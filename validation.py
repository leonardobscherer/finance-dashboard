import pandas as pd

def validate_header(headers):
    header_checklist = ['Data', 'Valor', 'Identificador', 'Descrição']
    missing_headers = [header for header in header_checklist if header not in headers]
    return missing_headers
           
def validate_values(df):
   if pd.api.types.is_float_dtype(df['Valor']) == False:
       df['Valor'] = df['Valor'].astype(float)
       print('The values have been converted to Float')

