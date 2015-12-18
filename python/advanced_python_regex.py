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
degree_frequencies =  pd.Series(degrees).value_counts()

## Q2
df['title'][24] = 'Assistant Professor of Biostatistics' # Correcting typo
title_frequencies = df['title'].value_counts()

## Q3
emails = list(df.email)

## Q4
email_re = re.compile("@[\w.]+")
domains = [email_re.search(email).group() for email in emails]
domain_frequencies = pd.Series(domains).value_counts()
