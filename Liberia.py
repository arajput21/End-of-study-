import requests
import pandas as pd
import numpy as np

data = {
    'token':'580C6A13EC7E1B5DEAF6D40C16B0C118',
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
    's_eos_sub_completed': 'eos_compl',
    's_eos_date_visit': 'eos_end_dt',
    's_eos_primary_withdrawal': 'eos_reason',
    's_eos_other_specify': 'end_other_specify',
    's_eos_dod': 'end_dod',
    's_eos_tod': 'end_tod',
    's_eos_final_comment': 'end_comment'
}
df.rename(columns=rename_dict, inplace=True)

# Set all values in 's_eos_cause' column to null (NaN)
if 's_eos_cause' in df.columns:
    df['s_eos_cause'] = np.nan

# Print the new column names and first few rows to check
print(df.columns.tolist())
