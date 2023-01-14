import altair as alt

def plot_ma_200days(moving_avg, period):
    """
    Plot stock price and corresponding 200 day moving average 
    for a specified period of time

    Parameters
    ----------
    moving_avg : list
        A list represting the 200 day moving average of a stock price for
        the period of available data
        
    period : int
        period of time for which the plot is created

    Returns
    --------
    Altair Chart
        A line chart showing price data and corresponding 200 day 
        moving averige line for a stock

    Examples
    --------
    >>> plot_ma_200days(moving_avg, 365)
    """
