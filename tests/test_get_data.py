import pandas as pd
import stocksignals.get_data as gd

def test_get_data():
    """
    Tests that the get_data function downloads and saves the data properly.
    Example
    -------
    >>> test_get_data()
    """
    stock = "MSFT"
    
    gd.get_data(stock)
    
    
    output = pd.read_csv('../../data/'+stock+'.csv')
    
    assert isinstance(output, pd.DataFrame), "Data cannot be read from directory data"
    assert ("Close" in output.columns),  "Date is not in column names"
    assert (len(output) > 0), "Data file is empty"


