import altair as alt
import yfinance as yf

def plot_ma_200days(stock_ticker, date):
    """
    Plot prices in the past 200 day period of a stock on a given date

    Parameters
    ----------
    stock_ticker : string
        Ticker of the stock such as 'MSFT'
    date : string
        Given date for stock picking

    Returns
    --------
    Altair Chart
        A line chart showing price changes in the past 200 day period

    Examples
    --------
    >>> plot_ma_200days('MSFT', '2023-01-10')
    """
