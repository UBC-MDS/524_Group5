import pandas as pd
from stocksignals.calc_moving_avg import moving_average as ma
from stocksignals.get_data import get_data

def test_moving_average():
    """
    Tests that the moving average function is working as intended.
    Example
    -------
    >>> test_moving_average()
    """
    get_data("MSFT")
    get_data("FFIE")
    output = ma("MSFT", 200)
    assert isinstance(output, pd.DataFrame), "Output is not a dataframe!"
    assert len(output.index) != 0, "Period must be greater than 0. Dataframe is empty!"
    assert len(output.columns) == 2, "Number of columns should only be 2: Date and moving average!"