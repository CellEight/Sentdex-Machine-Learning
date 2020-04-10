import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High','Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = 100*((df['Adj. High']-df['Adj. Low'])/df['Adj. Low'])
df['CHANGE_PCT'] = 100*((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'])

df = df[['Adj. Close', 'HL_PCT', 'CHANGE_PCT', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

df['label']  = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])

X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train,y_train)
accuracy = clf.score(X_test, y_test)
print(accuracy)
