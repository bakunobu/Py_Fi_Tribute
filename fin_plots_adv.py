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

my_conf: dictionary
    pass

3) Creating three plots
- candle;
- oclh;
- combined (candle + barchart)
Manual: https://github.com/matplotlib/mplfinance/blob/master/examples/customization_and_styles.ipynb
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

#title
my_title = 'DAX Index'
candle_conf = dict(type='candle',volume=False,figratio=(8,5),figscale=0.5)
# own colorsert (blue/red for up and down)
mc = mpf.make_marketcolors(up='b',down='r')
s  = mpf.make_mpf_style(marketcolors=mc)



#my_style = mpf.make_mpf_style(marketcolors=bl_re_col, gridcolor='black')
#mpf.plot(quotes, **kwargs,
#         title=my_title, ylabel='Index Level',
#         style=s)


mc = mpf.make_marketcolors(up='blue',down='red',
                           edge='inherit',
                           wick='black',
                           volume='in',
                           ohlc='i')
s  = mpf.make_mpf_style(marketcolors=mc)
'''
mpf.plot(quotes,**candle_conf,
         title=my_title, ylabel='Index Level',
         style=s)

ohlc_conf = candle_conf.copy()
ohlc_conf.update(type='ohlc')

mpf.plot(quotes,**ohlc_conf,
         title=my_title, ylabel='Index Level',
         style=s)
'''

candle_conf_bar = candle_conf.copy()
candle_conf_bar.update(volume=True)
"""
candle_conf_bar = dict(type='candle',
              figratio=(8,5),figscale=0.5, show_nontrading=True)
"""
mpf.plot(quotes,**candle_conf_bar,
         title=my_title, ylabel='Index Level',
         ylabel_lower = 'Volume',
         style=s)
