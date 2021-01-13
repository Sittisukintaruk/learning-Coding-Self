import pandas as pd
import seaborn as sns
import numpy as np
import requests
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
from PIL import Image
register_matplotlib_converters()

print(f'pandas   version: {pd.__version__}')
print(f'seaborn  version: {sns.__version__}')
print(f'requests version: {requests.__version__}')

time = pd.Timestamp.now()

print(time)

#ดึง API แปลงเป็น json
url='https://corona.lmao.ninja/jhucsse'
r=requests.get(url)
j=r.json()
print(j[:3])

print(type(j))

df=pd.DataFrame(j)


dstats=df['stats'].apply(pd.Series)
#dstats = pd.json_normalize(df.stats)
print(dstats)


dcoor=df['coordinates'].apply(pd.Series)
# dcoor = pd.json_normalize(df.coordinates)

ds= pd.concat([df[['country', 'province', 'updatedAt']], dstats, dcoor], axis=1)

print(ds)

#print(info)

ds['updatedAt'] = ds['updatedAt'].astype('datetime64') #แปลงค่า colurm datetime
cols=['confirmed', 'deaths', 'recovered', 'latitude', 'longitude']
ds[cols] = ds[cols].apply(pd.to_numeric, errors='coerce') #แปลงค่า colorm เป็น ตัวเลข int float

# ฟีลเตอร์
#ds = ds[ds['country']=='Thailand'] ฟีลเตอร์ ประเทศไทย
#ber = ds[['confirmed', 'deaths', 'recovered']].sum()
#br = ds[['country', 'confirmed', 'deaths', 'recovered']].groupby('country').sum()

dq = ds[ds['country'].str.contains('Thailand|Malaysia|Singapore|Indonesia|Cambodia')]
colors = ['.8' if c != 'Thailand' else 'salmon' for c in dq['country']]
plt.figure(figsize=(12, 5))
sns.barplot(data=dq, x='country', y='confirmed', palette=colors)
plt.title(f"COVID-19 as of {str(ds.loc[0,'updatedAt'])}");
plt.show()

columns =  ds.columns
info = ds.info()
message = "ประเทศไทย กาลาแล้น : "
print(info)
print(columns)
print("%s\n%s" %(message ,dq))

sum = ds.confirmed.sum()
print("ยอดผู้ติดเชื้อ : " , sum)



