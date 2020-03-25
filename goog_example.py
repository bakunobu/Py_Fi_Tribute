import numpy as np
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader as web
import matplotlib.pyplot as plt

# the original code just didn't work fine: no module pandas.io
# (is replaced by datareader (pip3 install pandas-datareader)
# some code before importing added (get an idea from StackOverflow
# and 'google' doesn't provide data anymore, so it is replaced with yahoo


goog = web.DataReader('GOOG', data_source='yahoo',
                      start='3/14/2009', end='4/14/2014')

#print(goog.tail())

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1)) # изменение курса (лог) по дням
goog['Volatility'] = goog['Log_Ret'].rolling(252).std() * np.sqrt(252) #doesn't work with rolling_std

#graph show

goog[['Close', 'Volatility']].plot(color='blue', figsize=(8, 6)) #the original code doesn't work (again)
plt.show()
