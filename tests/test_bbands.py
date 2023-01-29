import pandas as pd
import stocksignals.bbands as bb
from stocksignals.get_data import get_data

def test_get_bbands():
    """
    Tests that the Bollinger bands are calculated as expected
    and the return object is correct.
    Example
    -------
    >>> test_get_bbands()
    """
    get_data("MSFT")
    get_data("FFIE")
    
    output = bb.get_bbands("MSFT")
    assert isinstance(output, pd.DataFrame), "Output is not a dataframe!"
    assert len(output.index) != 0, "Period must be greater than 0. Dataframe is empty!"
    assert len(output.columns) == 2, "Number of columns should only be 2: Upper and lower band!"
