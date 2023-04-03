# -*- coding: utf-8 -*-
"""finalprojectvisualisation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FqC9N7zZT7tj3Nh1s-Q0HOPbZ1eplAh2

#Import Library
"""

import pandas as pd
import plotly
import numpy as np
#from dash import Dash, html
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime

# !pip3 install dash

from dash import Dash, html

"""#Read data and Clean data"""

df = pd.read_csv("rental_data.csv")
df.head(10)

df['Value'] = df['Value'].replace('-',0)
df.head(10)

df['Value'] = pd.to_numeric(df['Value'])

df = df[df['Year'] >= 2018]

df.isnull().sum()

#df[df['Suburb'] == 'Group Total']

df['Year'] = df['Year'].astype('str')

#df['Year'] = df['Year'].apply(lambda val: datetime.strptime(val, "%Y"))
df['Year'] = df['Year'].apply(lambda val: datetime.strftime(val, "%Y"))

count = df[df['Measure'] == 'Count']

mediandf = df[df['Measure'] == 'Median'].reset_index()

gpmedian = pd.DataFrame(mediandf.groupby(by=['Suburb','Year','Housing_Type'])['Value'].median().reset_index())
gpmedian.head(20)

"""#Build visualisation"""

onebedflat = gpmedian[gpmedian['Housing_Type'] == '1 bedroom flats']

Housing_Typels = gpmedian['Housing_Type'].unique()

Housing_Typels[1]

figls = []
for i in Housing_Typels:
    df = gpmedian[gpmedian['Housing_Type'] == i]
    fig = px.line(df, x="Year", y="Value", color='Suburb')
    fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Value',
    title= i,
    hovermode="x")
    fig.show()
    figls.append(fig)

figls[0].show()

fig = px.line(onebedflat, x="Year", y="Value", color='Suburb')
fig.show()







