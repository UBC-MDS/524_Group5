
def move_ave_10_20(stock_data):
    """
    Calculates simple moving average (SMA) of a stock price on a given date
    
    Parameters
    ----------
    data : a data file containing all available stock data
            from Yahoo finance
    
    Returns
    --------
    10_day_SMA : list
        A list with 10 day SMA of a stock price for 
        the period of available data
    20_day_SMA : list
        A list with 20 day SMA of a stock price for 
        the period of available data
    
    Examples
    --------
    >>> move_ave_10_20(MSFT_data)
    """
