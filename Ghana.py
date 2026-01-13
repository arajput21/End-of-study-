import requests
import pandas as pd
import numpy as np
def ReadGhana():   
    #!/usr/bin/env python
    data = {
        'token': '872D8B8556D4AC5E1A6CDA8C04364ADE',
        'content': 'record',
        'action': 'export',
        'format': 'json',
        'type': 'flat',
        'csvDelimiter': '',
        'fields[0]': 'patient_id',
        'forms[0]': 'end_of_study',
        'rawOrLabel': 'label',
        'rawOrLabelHeaders': 'label',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }
    r = requests.post('https://edc.aceso-sepsis.org/api/',data=data)

    dat1 = r.json()
    df = pd.DataFrame(dat1)
    new_columns = {col: col.replace('end', 's_eos', 1) if col.startswith('end') else col for col in df.columns}
    df.rename(columns=new_columns, inplace=True)
    # Add two new columns with NA values
    df['s_eos_cause'] = np.nan
    df['s_eos_final_comment'] = np.nan
     #drop unwanted columns
    df= df.drop(columns=['s_eos_of_study_complete','redcap_repeat_instance','redcap_repeat_instrument'])

#Filtering the DataFrame
def filtered_df(df):
    filtered_df = df[df['redcap_event_name'].str.contains('eos', case=False)]
    #return filtered_df(df)

    print('HTTP Status: ' + str(r.status_code))
    print(r.json())

    cols=df.columns
    print(cols)
    return filtered_df(df)

print('Ghana Alignment')




# Rename columns starting with 'end' to start with 's_eos' instead
 
# Print the new column names
#print(filtered_df.columns.tolist())
#print(filtered_df.head())

#calculate the number of patients
#num_patients = filtered_df['patient_id'].count()
#print(f'Number of patients: {num_patients}')

# Transpose the DataFrame
#key_cols = ['patient_id', 'redcap_event_name']
#value_cols = [c for c in Filtered_df.columns if c.startswith('s_eos')]


#long_df = Filtered_df.melt(id_vars=key_cols, value_vars=value_cols,
#                           var_name='Name', value_name='Value')
#summary=(long_df
#         .groupby( ['Name', 'Value'],dropna=False).size()
#         .reset_index(name='Count')
#        )
#summary=summary.sort_values(by=['Name','Value'])
#print("summary is:", summary)