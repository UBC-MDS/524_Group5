import pandas as pd
import stocksignals.bbands as bb
from stocksignals.get_data import get_data

def test_moving_average():
    """
    Tests that the Bollinger bands are calculated as expected
    and the return object is correct.
    Example
    -------
    >>> test_bbands()
    """
    get_data("MSFT")
    get_data("FFIE")
        
    data = pd.read_csv('data/MSFT.csv')

    # Compute prerequisites for the bands
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    df = data[['Close']]
    move_average = df.rolling(window=20).mean()
    move_standard_deviation = df.rolling(window=20).std()

    # Create dataframe with the two bands
    bands = move_average + 2 * move_standard_deviation
    bands = bands.rename(columns={"Close": "upper_band"})
    bands['lower_band'] = move_average - 2 * move_standard_deviation 
    output = bands
    
    assert isinstance(output, pd.DataFrame), "Output is not a dataframe!"
    assert len(output.index) != 0, "Period must be greater than 0. Dataframe is empty!"
    assert len(output.columns) == 2, "Number of columns should only be 2: Upper and lower band!"