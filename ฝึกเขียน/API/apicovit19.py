import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
time = pd.Timestamp.now()
print(f'pandas version:  {pd.__version__}')
print(f'requests version: {requests.__version__}')


url='https://corona.lmao.ninja/all'
r=requests.get(url)
j=r.json()
times = pd.datetime.fromtimestamp(j['updated'] // 1000).strftime('%Y-%m-%d %H:%M:%S')
print(j)

