import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests


url='https://corona.lmao.ninja/countries'
r=requests.get(url)
j=r.json()

print(type(j))

df=pd.DataFrame(j)
print(df)

thai = df[df.country=='Thailand']
print(thai)
thai.to_csv('covid19_latest.csv', index=False)
df.to_excel('covid19_latest.xlsx', index=False)
