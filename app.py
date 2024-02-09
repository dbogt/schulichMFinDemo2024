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
yearsData = list(df.index.year.unique())

#year1 = st.sidebar.selectbox("Pick a start year", yearsData)
#year2 = st.sidebar.selectbox("Pick an end year", yearsData) #last year
start_date = st.sidebar.date_input('Start Date', df.index.min())
end_date = st.sidebar.date_input('End Date', df.index.max())

#df = df.loc[str(year1):str(year2)]
            #df.loc['2016':'2018']
df = df.loc[start_date:end_date]

df['Returns'] = df['Adj Close'].pct_change()

#Create a chart
fig = px.line(df, y='Adj Close')


figHist = px.histogram(df, x=df['Returns'], nbins=100)
figHist.update_layout(
    title='Distribution of Daily Returns',
    xaxis_title='Daily Returns',
    yaxis_title='Frequency',
)



#Outputs
st.title("Web App - Schulich Class")
st.write("Demo example from Training the Street class")
st.plotly_chart(fig) #output plotly graph
st.plotly_chart(figHist)
st.write(df) #similar to print, but will show it in the app


    #in the console type:   !streamlit run app.py





