import yfinance as yf

def get_bbands(stock_ticker, rate = 20):
    """
    Calculates upper and lower Bollinger bands for a stock using
    a day-range; default day range = 20 days
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
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
    >>> bbands('MSFT')
    """