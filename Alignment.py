# define all our imports
import requests
import csv
import os
import pandas as pd
import json
import numpy as np
import LiberiaAlignment as la
import MadagascarAlignment as mad
import PeruAlignment as per
import GhanaAlignment as ga
import CambodiaAlignment as cam
import DukeAlignment as du
import UgandaAlignment as ug

def InitializeDataFrame():
    cols =  cols =  ['PID','Atyx_FieldName','Study','Value','FieldType','FieldLabel','Units','Volume/Dose/Rate','TimePoint','Repeat']
    Infusionsdf = pd.DataFrame(columns=cols)

    return Infusionsdf   

# Main program
Infusionsdf = InitializeDataFrame() # initialize Dataframe to begin

# Process Liberia
df = la.ReadLiberia()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = la.ParseLiberiaRow(row,df = Infusionsdf)

# Process Madagascar
df = mad.ReadMadagascar()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = mad.ParseMadagascarRow(row,df = Infusionsdf)

# Process Peru
df = per.ReadPeru()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = per.ParsePeruRow(row,df = Infusionsdf)

# Process Ghana
df = ga.ReadGhana()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = ga.ParseGhanaRow(row,df = Infusionsdf)

# Process Ghana
df = cam.ReadCambodia()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = cam.ParseCambodiaRow(row,df = Infusionsdf)

# Process duke
df = du.ReadDuke()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = du.ParseDukeRow(row,df = Infusionsdf)

# Process duke
df = ug.ReadUganda()
for i in range(len(df)):
    row = df.iloc[i]
    Infusionsdf = ug.ParseUgandaRow(row,df = Infusionsdf)

print(Infusionsdf)
print(Infusionsdf.head())
Infusionsdf.to_csv('InfusionOutput.csv', index=False)