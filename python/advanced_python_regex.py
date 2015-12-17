import pandas as pd
import re


df = pd.read_csv('faculty.csv')
df.columns = [col.strip() for col in df.columns] #Fixing column names


## Q1

degree_strings = list(df['degree'].values)
# Cleaning the entries so that they are uniform
degree_lists = [d.strip().split(' ') for d in degree_strings]
degrees = [degree.replace('.','').upper() for sublist in degree_lists\
										  for degree in sublist]
del degrees[degrees.index('0')] # Removing the non-degree from list
frequencies =  pd.Series(degrees).value_counts()/len(pd.Series(degrees))
print frequencies

## Q2

# df['title'][24] = 'Assistant Professor of Biostatistics' # Correcting typo
# print df['title'].value_counts()/len(df['title'])