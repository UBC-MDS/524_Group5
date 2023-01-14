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
        A list with lower band values of 2 standard deviations above
        20-day moving average 
    Examples
    --------
    >>> bbands(MSFT_data)
    """