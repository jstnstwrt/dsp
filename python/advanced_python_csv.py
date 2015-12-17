import pandas as pd
from advanced_python_regex import emails

df = pd.DataFrame(emails)
df.to_csv('emails.csv', header = False, index = False)