import yfinance as yf
import os

def get_data(stock_ticker):
    """
    Downloads all available historical histocical daily data 
    for stock_ticker from Yahoo finance and stores it as a 
    csv file in data folder. If data folder does not exist
    it is created.
    
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
    
    # Create DataFrame with the stock history data
    
    ticker = yf.Ticker(stock_ticker)
    hist = ticker.history(period="max", interval='1d')
    
    # Define output path for saving the data to a csv file
    out_file = "../../data/"+stock_ticker+".csv"

    # Reset index of dataframe in order to retain dates
    hist.reset_index()
    
    
    # Save the DataFrame to a data directory 
    # and make directory if it doesn't exist
    try:
        hist.to_csv(out_file)
    except:
        os.makedirs(os.path.dirname(out_file))
        hist.to_csv(out_file, index=False)