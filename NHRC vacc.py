import requests
import pandas as pd
import numpy as np

data = {
    'token':'E80CA975DAE899C6B631ED433B15B410',
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

# Rename columns as specified
rename_dict = {
    'eos_stop': 's_eos_sub_completed',
    'eos_dt': 's_eos_date_visit',
    'eos_nolonger': 's_eos_primary_withdrawal',
    'end_reason': 's_eos_other_specify',
}
df.rename(columns=rename_dict, inplace=True)

# Set all values in specified columns to null (NaN)
df['s_eos_cause'] = np.nan
df['s_eos_dod'] = np.nan
df['s_eos_tod'] = np.nan
df['s_eos_final_comment'] = np.nan

#deselecting columns
df=df.loc[:, ~df.columns.str.startswith('end_')]

# Print the new column names and first few rows to check
print(df.columns.tolist())
