import requests
import pandas as pd
import numpy as np

data = {
    'token':'A7F015CB5A97607D26E0BF94F3989E2B',
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

r = requests.post('https://edc-prod-az.aceso-sepsis.org/api/',data=data)
dat1 = r.json()
df = pd.DataFrame(dat1)

# Rename columns
rename_dict = {
    'end_reason':'s_eos_sub_completed',
    'end_last_date': 's_eos_date_visit',
    'end_primary_withdrawal': 's_eos_primary_withdrawal',
    'end_other_specify': 's_eos_other_specify',
    'end_dod': 's_eos_dod',
    'end_tod': 's_eos_tod',
   }

df.rename(columns=rename_dict, inplace=True)

# Set all values in specified columns to null (NaN)

df['s_eos_cause'] = np.nan
df['s_eos_final_comment'] = np.nan

#deselecting columns
df=df.loc[:, ~df.columns.str.startswith('end_')]

# Print the new column names and first few rows to check
print(df.columns.tolist())