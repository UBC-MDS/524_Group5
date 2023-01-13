import altair as alt
import yfinance as yf

def plot_ma_10_20(stock_ticker, date):
    """
    Plot prices in the past 20 day period and corresponding 10 day SMA and 20 day SMA of a stock on a given date
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
    date : string
        Given date for stock picking
    
    Returns
    --------
    Altair Chart
        A line chart shows price changes in the past 20 day period and corresponding 10 day SMA and 20 day SMA 
    
    Examples
    --------
    >>> plot_ma_10_20('MSFT', '2023-01-10')
    """
