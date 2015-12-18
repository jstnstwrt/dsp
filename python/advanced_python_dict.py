import pandas as pd
import numpy as np

df = pd.read_csv('faculty.csv')
df.columns = [col.strip() for col in df.columns] #Fixing column names


# Q6

# Getting last names for dict key
keys = df['name'].values.tolist()
names = [fullname.strip().split(' ') for fullname in keys]
last_names = [name[-1] for name in names]
# Fixing titles to be correct form
df['title'] = df['title'].map(lambda x: x.strip(' of Biostatistics'))
# Grabbing the rest of the data for our dictionary values
vals = df[['degree','title','email']].values.tolist()

faculty_dict = {}
for key, val in zip(last_names,vals):
	if key in faculty_dict:
		faculty_dict[key].append(val)
	else:
		faculty_dict[key] = [val]


# Q7

# Need to first adjust the keys to have (first,last)
first_last = [(name[0],name[-1]) for name in names] 
professor_dict = {key:value for key,value in zip(first_last,vals)}



# Q8

# Sort keys by the last name and print
sorted_keys = sorted(professor_dict, key=lambda x: x[1])
for key in sorted_keys[0:3]:
	print '%s:%s' % (key,professor_dict[key]) 
