import pandas as pd

def move_ave_200days(stock_data):
    """
    Calculates the 200 day moving average of a stock price on a given date

    Parameters
    ----------
    data : a data file containing all available stock data
            from Yahoo finance

    Returns
    --------
    moving_avg : list
        A list represting the 200 day moving average of a stock price for
        the period of available data

    Examples
    --------
    >>> move_ave_200days(MSFT_data)
    """
    data = pd.read_csv('data/'+stock_data+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = data.rolling(window=200).mean()
    mov_avg.index = data.index
    return mov_avg

print(move_ave_200days("MSFT"))