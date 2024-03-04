import pandas as pd
import numpy as np
import os
from sys import platform

#print (platform)

if platform == "darwin":
    os.chdir('/Users/dhyanadesai/Downloads')
else:
    os.chdir('C:\\Users\\anany\\Downloads')


file = 'FullData2.csv'
fields = ['ID', 'TRUEAGE' ,'DTH00_02', 'B11_2', 'B21_2','B27_2','B26_2', 'B24_2', 'D11H_2',
          'DTH02_05', 'B11_5', 'B21_5','B27_5','B26_5', 'B24_5', 'D11H_5',
          'DTH05_08', 'B11_8', 'B21_8','B27_8','B26_8', 'B24_8', 'D11H_8',
          'DTH08_11', 'B11_11', 'B21_11','B27_11','B26_11', 'B24_11', 'D11H_11']

# 00 02 05 08 11 14

df = pd.read_csv(file, usecols=fields, low_memory=False)

df.columns = ['ID', 'AGE_SURVEY', 'DEATH_2', 'OP_QUAL_2', 'OP_BRIGHT_2', 'OP_YOUNG_2', 'OP_USE_2', 'SO_LONE_2', 'SO_ACT_2',
              'DEATH_5', 'OP_QUAL_5', 'OP_BRIGHT_5', 'OP_YOUNG_5', 'OP_USE_5', 'SO_LONE_5', 'SO_ACT_5',
              'DEATH_8', 'OP_QUAL_8', 'OP_BRIGHT_8', 'OP_YOUNG_8', 'OP_USE_8', 'SO_LONE_8', 'SO_ACT_8',
              'DEATH_11', 'OP_QUAL_11', 'OP_BRIGHT_11', 'OP_YOUNG_11', 'OP_USE_11', 'SO_LONE_11', 'SO_ACT_11']

#hi
# print(df.head(5))


df.to_csv('Data.csv')
