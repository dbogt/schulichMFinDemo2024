# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:30:39 2024

@author: Bogdan Tudose
@email: bogdan.tudose@trainingthestreet.com

"""
#Import packages
import streamlit as st
import pandas as pd
import plotly.express as px

#Grab Data
tickers = ['AAPL','DIS','NKE']
ticker = st.sidebar.selectbox("Pick a ticker:",tickers)
df = pd.read_csv(ticker + '.csv', parse_dates=['Date'],
                 index_col=['Date'])

#Filter the data
year = st.sidebar.selectbox("Pick a year", [2015,2016,2017])
df = df.loc[str(year)]


#Create a chart
fig = px.line(df, y='Adj Close')
#Outputs
st.title("Web App - Schulich Class")
st.write("Demo example from Training the Street class")
st.plotly_chart(fig) #output plotly graph
st.write(df) #similar to print, but will show it in the app


    #in the console type:   !streamlit run app.py





