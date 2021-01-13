import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests

country='thailand'
url=f'https://corona.lmao.ninja/countries/{country}'
rt=requests.get(url)
thai =rt.json()

print(thai)
print("thai cases: ",thai["cases"])
print("thai Today: ",thai["todayCases"])
print("thai deaths: ",thai["deaths"])
print("thai todayDeaths: ",thai["todayDeaths"])
print("thai recovered: ",thai["recovered"])
print("thai active: ",thai["active"])
print("thai critical: ",thai["critical"])
print("thai casesPerOneMillion: ",thai["casesPerOneMillion"])

level = 0
if thai["cases"] > 1000:
    level = 3
    print("ประเทศไทยมีระดับความรุนแรง : ",level)
elif thai["cases"] < 1000 and thai["cases"] > 500:
    level = 2 
    print("ประเทศไทยมีระดับความรุนแรง : ",level)
else:
    level = 1
    print("ประเทศไทยมีระดับความรุนแรง : ",level)














