# -*- coding: utf-8 -*-
"""Getting started with pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoUjF3WCGWN6_P39BLhnCbTKxswWfN8Z
"""

import io
import pandas as pd

from google.colab import files
uploaded = files.upload()

print (uploaded['nyc_weather.csv'][:200].decode('utf-8') + '...')

import pandas as pd
import io

df = pd.read_csv(io.StringIO(uploaded['nyc_weather.csv'].decode('utf-8')))
df.head(4)

print(df['Temperature'].max())

print(df['EST'][df['Events']=='Rain'])

print(df[['EST','CloudCover']][df['Events']=='Rain'])

p=df[['EST','Temperature']].loc[df['Temperature'].idxmax()]

#print(p)

day=df['Temperature'].max()
#print(day)

print(df['EST'][df['Temperature']==day])