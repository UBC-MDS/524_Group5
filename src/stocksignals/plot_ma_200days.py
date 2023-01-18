import matplotlib.pyplot as plt
from move_ave_200days import *
import pandas as pd

def plot_ma_200days(stock, period):
    """
    Plot stock price and corresponding 200 day moving average 
    for a specified period of time

    Parameters
    ----------
    moving_avg : list
        A list representing the 200 day moving average of a stock price for
        the period of available data
        
    period : int
        period of time for which the plot is created

    Returns
    --------
    Altair Chart
        A line chart showing price data and corresponding 200 day 
        moving average line for a stock

    Examples
    --------
    >>> plot_ma_200days(moving_avg, 365)
    """

    start_date = '2015-01-01'
    end_date = '2016-12-31'
    
    data = pd.read_csv('data/'+stock+'.csv')
    mov_avg = move_ave_200days(stock)
    print(data)

    plt.figure(figsize=(16,9))
    plt.plot(data.loc[500:700, "Close"].index, data.loc[500:700, "Close"], label='Price')
    plt.plot(mov_avg.loc[500:700, "Close"].index, mov_avg.loc[500:700, "Close"], label = '200-days SMA')
    plt.legend()
    plt.show()

plot_ma_200days("MSFT")

