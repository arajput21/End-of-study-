import requests
import pandas as pd
import numpy as np

data = {
    'token': '01C90E42CB949766B6B11344ACF0E3FB',
    'content': 'record',
    'action': 'export',
    'format': 'json',
    'type': 'flat',
    'csvDelimiter': '',
    'fields[0]': 'patient_id',
    'forms[0]': 'end_of_study',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
r = requests.post('https://edc.aceso-sepsis.org/api/', data=data)
dat1 = r.json()
df = pd.DataFrame(dat1)

# Rename columns starting with 'end' to start with 's_eos' instead
new_columns = {col: col.replace('end', 's_eos', 1) if col.startswith('end') else col for col in df.columns}
df.rename(columns=new_columns, inplace=True)

# Add two new columns with NA values
df['s_eos_cause'] = np.nan
# Print the new column names
print(df.columns.tolist())