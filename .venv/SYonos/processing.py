import pandas as pd
import numpy as np
import os
from sys import platform


if platform == "darwin":
    os.chdir('/Users/dhyanadesai/Downloads')
else:
    os.chdir('C:\\Users\\anany\\Downloads')


file = 'Data.csv'
# 00 02 05 08 11

#
# df.columns = ['ID', 'AGE_SURVEY', 'DEATH_2', 'OP_QUAL_2', 'OP_BRIGHT_2', 'OP_YOUNG_2', 'OP_USE_2', 'SO_LONE_2', 'SO_ACT_2',
#               'DEATH_5', 'OP_QUAL_5', 'OP_BRIGHT_5', 'OP_YOUNG_5', 'OP_USE_5', 'SO_LONE_5', 'SO_ACT_5',
#               'DEATH_8', 'OP_QUAL_8', 'OP_BRIGHT_8', 'OP_YOUNG_8', 'OP_USE_8', 'SO_LONE_8', 'SO_ACT_8',
#               'DEATH_11', 'OP_QUAL_11', 'OP_BRIGHT_11', 'OP_YOUNG_11', 'OP_USE_11', 'SO_LONE_11', 'SO_ACT_11']

df = pd.read_csv(file)
df.reset_index(inplace=True)

df['DEATH_YEAR'] = 0

for index, row in df.iterrows():
    for year in {2,5,8,11}:
        if row[f'DEATH_{year}'] == 1:
            df.at[index, 'DEATH_YEAR'] = 2000 + year
            break


# start = df.shape[0]
# print(start)

df = df.drop(df[df['DEATH_YEAR']==0].index)



end =  df.shape[0]


# print(end)

df['LIFESPAN'] = df['AGE_SURVEY'] + (df['DEATH_YEAR'] - 1998)



# df = df.drop(df[df['OP_BRIGHT_2']<=0].index)
# df = df.drop(df[df['OP_BRIGHT_2']>5].index)
# df = df.drop(df[df['OP_QUAL_2']<=0].index)
# df = df.drop(df[df['OP_QUAL_2']>5].index)


for index, row in df.iterrows():
    if (row['OP_BRIGHT_2'] <= 0 or row['OP_BRIGHT_2'] > 5) or row['OP_QUAL_2'] <= 0 or row['OP_QUAL_2'] > 5:
        lifespan = row['LIFESPAN']
        df.at[index, 'OP_BRIGHT_2'] = 5 - (4*((lifespan-82)/(46)))
        df.at[index, 'OP_QUAL_2'] = 5 - (4 * ((lifespan - 82) / (46)))

# df = df.drop(df[df['SO_LONE_2']<=0].index)
# df = df.drop(df[df['SO_LONE_2']>5].index)
# df = df.drop(df[df['SO_ACT_2']<=0].index)
# df = df.drop(df[df['SO_ACT_2']>5].index)


for index, row in df.iterrows():
    if (row['SO_LONE_2'] <= 0 or row['SO_LONE_2'] > 5) or row['SO_ACT_2'] <= 0 or row['SO_ACT_2'] > 5:
        lifespan = row['LIFESPAN']
        df.at[index, 'SO_LONE_2'] = 5 - (4*((lifespan-82)/(46)))
        df.at[index, 'SO_ACT_2'] = (4 * ((lifespan - 82) / (46))) + 1

# print(df.shape[0])

# print(df[['LIFESPAN']].describe())

df['OP'] = 6-((df['OP_BRIGHT_2'] * 0.5) + (df['OP_QUAL_2'] * 0.5))
df['SO'] = ((6 - df['SO_LONE_2']) * 0.5) + (df['SO_ACT_2'] * 0.5)

df1 = df[['LIFESPAN', 'OP', 'SO']]



# print(df.head(5)['OP'])
# print(df.head(5)['SO'])
#
#
# print(df[['OP']].describe())
# print(df[['SO']].describe())


# print(start - end)


# print(df.head(5)['DEATH_2'])
# print(df.head(5)['DEATH_YEAR'])
# print(df.head(5)['AGE_SURVEY'])
# print(df.head(5)['LIFESPAN'])






df1.to_csv('DataProcessed.csv')

# hi
# print(df.head(5))


