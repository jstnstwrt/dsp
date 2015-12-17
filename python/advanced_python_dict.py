import pandas as pd
import numpy as np

df = pd.read_csv('faculty.csv')
df.columns = [col.strip() for col in df.columns] #Fixing column names

# Getting last names for dict key
keys = df['name'].values.tolist()
names = [fullname.strip().split(' ') for fullname in keys]
last_names = [name[-1] for name in names]
# Fixing titles to be correct form
df['title'] = df['title'].map(lambda x: x.strip(' of Biostatistics'))

# Creating dict
vals = df[['degree','title','email']].values.tolist()
faculty_dict = {}
for key, val in zip(last_names,vals):
	if key in faculty_dict:
		faculty_dict[key].append(val)
	else:
		faculty_dict[key] = [val]

print faculty_dict

