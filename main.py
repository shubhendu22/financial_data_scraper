import streamlit as st
import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

st.title("Financial Data Scraping for Corporate Performance Analysis")
st.write("Welcome to the go to place for stock data")
stock_name=st.selectbox("Select stock",("AAPL","AMZN","TWTR","AMD","F"))
st.write(stock_name)
aapl_df = yf.download(stock_name, 
                      start='2019-01-01', 
                      end='2021-06-12', 
                      progress=False,
)
st.write(aapl_df.head())