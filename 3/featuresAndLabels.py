import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = 100*((df['Adj. High']-df['Adj. Low'])/df['Adj. Low'])
df['CHANGE_PCT'] = 100*((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'])

df = df[['Adj. Close', 'HL_PCT', 'CHANGE_PCT', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label']  = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())
