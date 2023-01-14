import yfinance as yf

def move_ave_200days(stock_ticker, date):
    """
    Calculates the 200 day moving average of a stock price on a given date

    Parameters
    ----------
    stock_ticker : string
        Ticker of the stock such as 'MSFT'
    date : string
        Given date for stock picking

    Returns
    --------
    moving_avg : float
        A float represting the 200 day moving average of a stock price on a given date

    Examples
    --------
    >>> move_ave_200days('MSFT', '2023-01-10')
    """
