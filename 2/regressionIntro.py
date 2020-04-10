import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = 100*((df['Adj. High']-df['Adj. Low'])/df['Adj. Low'])
df['CHANGE_PCT'] = 100*((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'])

df = df[['Adj. Close', 'HL_PCT', 'CHANGE_PCT', 'Adj. Volume']]

print(df.head())
