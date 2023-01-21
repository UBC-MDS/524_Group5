from stocksignals.plot_ma_200days import plot_ma_200days
from unittest.mock import patch
import matplotlib.pyplot as plt
import pandas as pd
from pytest import raises

def test_plot_ma_200days():
    """
    Test input, plot showing and legend for plot_ma_200days()
    Example
    -------
    >>> test_plot_ma_200days()
    """
    # check invalid input
    with raises(TypeError) as error_symbol:
        plot_ma_200days(123)
    
    # check the number of figure created after calling plot_ma_200days() function
    plt.close()
    plot_ma_200days('MSFT')
    assert plt.gcf().number == 1, "The number of plot created is incorrect!"

    # Assert plt.show got called
    with patch("stocksignals.plot_ma_200days.plt.show") as show_patch:
        plot_ma_200days('MSFT')
        assert show_patch.called, "Showing plot is called incorrectly!"
    
    # Assert plt.figure got called
    with patch("stocksignals.plot_ma_200days.plt.legend") as legend_patch:
        plot_ma_200days('MSFT')
        assert legend_patch.called, "Plot legend is not created correctly!"