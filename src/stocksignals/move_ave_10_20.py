import yfinance as yf

def move_ave_10_20(stock_ticker, date):
    """
    Calculates simple moving average (SMA) of a stock price on a given date
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
    date : string
        Given date for stock picking
    
    Returns
    --------
    numerical_list : list
        A list with 10 day SMA and 20 day SMA of a stock price on a given date
    
    Examples
    --------
    >>> move_ave_10_20('MSFT', '2023-01-10')
    """
