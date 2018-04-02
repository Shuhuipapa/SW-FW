# Import all libraries needed
import pandas as pd
import xlsxwriter
from numpy import random

Textfile = r'C:\users\sding\PycharmProjects\SW-FW\example data.txt'
data = pd.read_csv(Textfile, sep='\t')
data = data.drop(['Line','MM/DD/YY hh:mm:ss.ms.us'], axis=1)
print(data)
writer = pd.ExcelWriter(r'C:\users\sding\PycharmProjects\SW-FW\example data.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name='sheet1')

def