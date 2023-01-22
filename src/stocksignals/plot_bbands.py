import matplotlib.pyplot as plt
from stocksignals import bbands as bb
import pandas as pd

def plot_bbands(stock_symbol):
    """
    Plot stock price and corresponding upper and lower Bollinger bands
    for the last 200 trading days.
    
        Parameters
    ----------        
    stock_symbol : string
        Ticker symbol of the stock for which the plot is created
    Returns
    --------
    Matplotlib chart
        A line chart showing price data and corresponding upper
        and lower Bollinger bands.
    Examples
    --------
    >>> plot_bbands("MSFT")
    """
    
    # Check if stock_symbol is a string
    if not isinstance(stock_symbol, str):
        raise TypeError("Sorry, the input must be a string")

        
    # Load the data
    data = pd.read_csv('../../data/'+stock_symbol+'.csv')
    data["Date"] = pd.to_datetime(data["Date"], utc=True).dt.date

    
    # Obtain a DataFrame with the Bollinger bands
    bbands = bb.get_bbands(stock_symbol).reset_index()

    # Create a plot with closing price surrounded by the two bands
    plt.figure(figsize=(8,6))
    plt.plot(data.iloc[-200:, 0],  # date
             data.iloc[-200:, 4], "b-", label='Price')  # close
    plt.plot(bbands.iloc[-200:, 0],
             bbands.iloc[-200:, 1], "r--", label = 'Upper Bollinger band')
    plt.plot(bbands.iloc[-200:, 0],
             bbands.iloc[-200:, 2], "g--", label = 'Lower Bollinger band')
    plt.xticks(rotation=90)
    plt.xlabel("Date (YYYY-MM)")
    plt.ylabel("Price level (USD)")
    plt.title(f"20-day Bollinger bands vs closing price {stock_symbol}")
    plt.legend()
    plt.show()