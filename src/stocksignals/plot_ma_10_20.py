import altair as alt

def plot_ma_10_20(10_day_SMA, 20_day_SMA, period):
    """
    Plot prices over a specified period
    and corresponding 10 day SMA and 20 day SMA of a stock
    
    Parameters
    ----------
    10_day_SMA : list
        A list with 10 day SMA of a stock price for 
        the period of available data
    20_day_SMA : list
        A list with 20 day SMA of a stock price for 
        the period of available data
    period : int
        period of time for which the plot is created
    
    Returns
    --------
    Altair Chart
        A line chart shows price changes during the specified period
        and corresponding 10 day SMA and 20 day SMA 
    
    Examples
    --------
    >>> plot_ma_10_20(10_day_SMA, 20_day_SMA, 365)
    """
