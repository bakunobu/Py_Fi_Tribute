"""
An advanced version of new financial graphs using the new mplfinance library


Fixes:
======
- Custom colour schemes
- Users labels and legends
- Users format of all the elements of figures

Elements:
=========
1) Getting data (using pandas_datareader library)

quotes: pd.DataFrame
    some data in DataFrame for some stock index

2) Creating a user's config data

candle_conf: dictionary
    type: str
        graph, value='candle'
    volume: bool
        adds a barchart for trade volume per day if True
    figratio: tuple
        fugure size (width, heigth)
    figscale: float
        scales aspect ratio
     

3) Creating three plots
- candle;
- oclh;
- combined (candle + barchart)

Manual by the library authors:
==============================
https://github.com/matplotlib/mplfinance/blob/master/examples/customization_and_styles.ipynb
"""


import mplfinance as mpf #!pip3 install --upgrade mplfinance
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas.util.testing import assert_frame_equal
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as dates

#getting historical data for 'DAX Index'
quotes = web.DataReader('^GDAXI', data_source='yahoo', #don't use 'google' as a data_source
                      start='5/1/2014', end='6/30/2014')



#graph 1 - candle
#base params dict
candle_conf = dict(type='candle',volume=False,figratio=(8,5),figscale=0.5)

#custom colorsert (blue/red for up and down)

mc = mpf.make_marketcolors(up='blue',down='red',
                           edge='inherit',
                           wick='black',
                           volume='in',
                           ohlc='i')
s  = mpf.make_mpf_style(marketcolors=mc)
#plot
mpf.plot(quotes,**candle_conf,
         title=my_title, ylabel='Index Level',
         style=s)

#graph 2 - ohlc
#base params = copy candle params and modify
ohlc_conf = candle_conf.copy()
ohlc_conf.update(type='ohlc')
#plot
mpf.plot(quotes,**ohlc_conf,
         title=my_title, ylabel='Index Level',
         style=s)

#graph 3 - candle + volume
#base params = copy candle params + volume=True
candle_conf_bar = candle_conf.copy()
candle_conf_bar.update(volume=True)
#plot
mpf.plot(quotes,**candle_conf_bar,
         title=my_title, ylabel='Index Level',
         ylabel_lower = 'Volume',
         style=s)
