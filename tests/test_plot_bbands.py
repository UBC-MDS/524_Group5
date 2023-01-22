from stocksignals.plot_bbands import plot_bbands
from unittest.mock import patch
import matplotlib.pyplot as plt
import pandas as pd
from pytest import raises

def test_plot_bbands():
    """
    Test input, plot showing and legend for plot_bbands()
    Example
    -------
    >>> test_plot_bbands()
    """
    # check invalid input
    with raises(TypeError) as error_symbol:
        plot_bbands(123)

    # check the number of figure created after calling plot_bbands() function
    plt.close()
    plot_bbands('FFIE')
    assert plt.gcf().number == 1, "The number of plots created is incorrect!"

    # Assert plt.show got called
    with patch("stocksignals.plot_bbands.plt.show") as show_patch:
        plot_bbands('FFIE')
        assert show_patch.called, "Showing plot is called incorrectly!"

    # Assert plt.figure got called
    with patch("stocksignals.plot_bbands.plt.legend") as legend_patch:
        plot_bbands('FFIE')
        assert legend_patch.called, "Plot legend is not created correctly!"