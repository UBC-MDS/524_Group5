import altair as alt

def plot_bbands(upper_band, lower_band):
    """
    Plot stock price along with upper and lower Bollinger band
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
    upper_band : list
        A list with upper band values of 2 standard deviations above
        specified moving average
    lower_band : list
        A list with lower band values of 2 standard deviations above
        specified moving average
    
    Returns
    --------
    Altair Chart
        A chart with stock price along with upper and lower bands
    
    Examples
    --------
    >>> plot_bbands('MSFT', upper_band, lower_band)
    """