import sys
sys.path.append('../src/stocksignals')

from plot_ma_10_20 import plot_ma_10_20days
from unittest.mock import patch
import matplotlib.pyplot as plt

def test_plot_ma_10_20days():
    """
    """
    # check the number of figure created after calling plot_ma_10_20days() function
    plt.close()
    plot_ma_10_20days('FFIE')
    assert plt.gcf().number == 1, "The number of plot created is incorrect!"

    # Assert plt.show got called
    with patch("plot_ma_10_20.plt.show") as show_patch:
        plot_ma_10_20days('FFIE')
        assert show_patch.called, "Showing plot is called incorrectly!"
    
    # Assert plt.figure got called
    with patch("plot_ma_10_20.plt.legend") as legend_patch:
        plot_ma_10_20days('FFIE')
        assert legend_patch.called, "Plot legend is not created correctly!"