# define all our imports
import requests
import csv
import os
import pandas as pd
import json
import numpy as np
#import Liberia as la
#import Madagascar as mad
#import peru as per
import Ghana as ga
#import Cambodia as cam
import Uganda as ug
def main():
    ghana_df=ga.ReadGhana()
    uganda_df=ug.ReadUganda()
    dfs=[d for d in [ghana_df, uganda_df] if d is not None]
    final_df=pd.concat(dfs, ignore_index=True, sort=False)
    print(final_df.shape)
    final_df.to_csv('final_output.csv', index=False)

if __name__ == "__main__":
     main()

