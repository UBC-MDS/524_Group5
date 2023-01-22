import pandas as pd
def get_bbands(stock_data, rate = 20):
    """
    Calculates upper and lower Bollinger bands for a stock using
    a day-range; default day range = 20 days
    
    Parameters
    ----------
    data : a data file containing all available stock data
            from Yahoo finance
    rate : int
        number of days, default = 20 days
    
    Returns
    --------
    bbands : DataFrame
        A Pandas DataFrame with upper and lower Bollinger band values
        for the period of availability of the data
    
    Examples
    --------
    >>> get_bbands("MSFT")
    """
    # Read stock data from saved file
    data = pd.read_csv('../../data/'+stock_data+'.csv')

    # Compute prerequisites for the bands
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    df = data[['Close']]
    move_average = df.rolling(window=20).mean()
    move_standard_deviation = df.rolling(window=20).std()

    # Create dataframe with the two bands
    bands = move_average + 2 * move_standard_deviation
    bands = bands.rename(columns={"Close": "upper_band"})
    bands['lower_band'] = move_average - 2 * move_standard_deviation
    
    return bands