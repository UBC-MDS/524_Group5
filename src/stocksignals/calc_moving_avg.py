import pandas as pd

def moving_average(stock_symbol, size):
    """
    Calculates the moving average of a stock price for a given range of dates

    Parameters
    ----------
    stock_symbol : string
        Ticker symbol of the stock for which the moving average is calculated    
    size : int
        Given range of dates in days for the moving average to be calculated
            
    Returns
    --------
    moving_avg : dataframe
        A dataframe representing the given day moving average of a stock price.

    Examples
    --------
    >>> moving_average('MSFT', 200)
    """
    data = pd.read_csv('data/'+stock_symbol+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = {}
    mov_avg[f"{size}MA"] = data["Close"].rolling(window=size).mean()
    moving_avg = pd.DataFrame(mov_avg).reset_index()
    return moving_avg
