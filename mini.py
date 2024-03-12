import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import plotly_express as px

import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv(r"C:\Users\shamb\Downloads\TrafficIndex_19Jun2022-26Jun20221.csv")

df.head()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test")
from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
df['location'] = df['City'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)

df

df['latitude']=df['point'].str[0]
df['longitude']=df['point'].str[1]

df

df.info()

df.sort_values(by="AverageTCI",ascending=True).tail(10).plot.barh(x='City',y='AverageTCI')

fig = px.scatter_mapbox(df,lat='latitude',lon='longitude',hover_name='City',hover_data=['AverageTCI'],color='AverageTCI',
    size="AverageTCI",size_max=20,opacity=0.4,
    center={'lat':50, 'lon':9},
    zoom=1,
    height=700,
    width=1000)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(title_text="City Map for Average TCI")
fig.show()

df.sort_values(by="MaxTCI",ascending=True).tail(10).plot.barh(x='City',y='MaxTCI')

'''fig = px.scatter_mapbox(df,lat='latitude',lon='longitude',hover_name='City',hover_data=['MaxTCI'],color='MaxTCI',
    size="MaxTCI",size_max=20,opacity=0.4,
    center={'lat':50, 'lon':9},
    zoom=1,
    height=700,
    width=1000)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.update_layout(title_text="City Map for Max TCI")
fig.show()'''

df[df['City']=='Tokyo']

df[df['City']=='Mumbai']

df[df['City']=='Jakarta']

df[df['City']=='London']

df.sort_values(by="MaxTCI",ascending=True).tail(12).plot.barh(x='City',y='MaxTCI')

df.sort_values(by="AverageTCI",ascending=True).tail(15).plot.barh(x='City',y='MaxTCI')




