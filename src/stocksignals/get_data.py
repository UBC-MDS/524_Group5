import yfinance as yf

def get_data(stock_ticker):
    """
    Downloads all available historical histocical daily data for stock_ticker from Yahoo finance
    and stores it as a data file
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
    
    Returns
    --------
    None
    
    Examples
    --------
    >>> get_data("MSFT")
    """

