import pandas as pd
def get_bbands(stock_data, rate = 20):
    """
    Calculates upper and lower Bollinger bands for a stock using
    a day-range; default day range = 20 days
    
    Parameters
    ----------
    data : a data file containing all available stock data
            from Yahoo finance
    rate : int
        number of days, default = 20 days
    
    Returns
    --------
    upper_band : list
        A list with upper band values of 2 standard deviations above
        20-day moving average 
    lower_band : list
        A list with lower band values of 2 standard deviations below
        20-day moving average 
    Examples
    --------
    >>> get_bbands("MSFT")
    """
    data = pd.read_csv('../../data/'+stock_data+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    df = data[['Close']]
    move_average = df.rolling(window=rate).mean()
    move_standard_deviation = df.rolling(window=rate).std()
    upper_band = move_average + 2 * move_standard_deviation
    lower_band = move_average - 2 * move_standard_deviation
    upper_band = upper_band.rename(columns={'Close': 'upper'})
    lower_band = lower_band.rename(columns={'Close': 'lower'})
    upper_band = list(upper_band['upper'])
    lower_band = list(lower_band['lower'])
    return upper_band, lower_band