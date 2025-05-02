# coding: utf-8
import pandas as pd
import os


#Load data from an Excel file using Pandas
MYDIR = "./"
filename = os.path.join(MYDIR, 'sample_data.xlsx')

df = pd.read_excel(filename,
               sheet_name="Sheet1",
              engine='openpyxl',)
