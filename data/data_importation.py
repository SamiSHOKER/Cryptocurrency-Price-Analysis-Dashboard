# Importing Libraries
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
from datetime import date
yf.pdr_override()

today = date.today()
end = today.strftime('%Y-%m-%d')
start = "2013-04-28"

df = pdr.get_data_yahoo("BTC-USD" , data_source = "yahoo" , start =start, end = end )
df= df.reset_index()
df['Crypto-USD'] = 'BTC-USD'

print(df.head())

crypto = ['ETH-USD','BNB-USD','ADA-USD','SOL-USD','XRP-USD','LUNA1-USD','DOT-USD','DOGE-USD','AVAX-USD']

for i in crypto:
    df0 = pdr.get_data_yahoo(i , data_source = "yahoo" ,start = start ,end = end )
    df0['Crypto-USD'] = i
    df0 = df0.reset_index()
    df = pd.concat([df,df0])

print(df.head())
print(df.shape)
print(df["Crypto-USD"].value_counts())

df.to_csv('crypto.csv')