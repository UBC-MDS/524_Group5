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

    start_date = pd.to_datetime(period[0])
    end_date = pd.to_datetime(period[1])

    data = pd.read_csv('data/'+stock+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = move_ave_200days(stock)
    mov_avg["Date"] = data["Date"]

    plt.figure(figsize=(8,6))
    plt.plot(data.loc[start_date:end_date, "Date"],
             data.loc[start_date:end_date, "Close"], label='Price')
    plt.plot(mov_avg.loc[start_date:end_date, "Date"],  # index
             mov_avg.loc[start_date:end_date, "Close"], label = '200-days SMA')
    plt.legend()
    plt.show()

plot_ma_200days("MSFT", ('2022-10-02', '2023-01-10'))

