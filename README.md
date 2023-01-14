# stocksignals

Calculate buy/sell signal indicators for a stock!

## Installation

```bash
$ pip install stocksignals
```

## Usage

```bash
import stocksignals
import matplotlib.pyplot as plt
import yfinance as yf


# Generage signals and plots
move_ave_10_20(stock_ticker, date)
plot_ma_10_20(stock_ticker, date)
move_ave_200days(stock_ticker, date)
plot_ma_200days(stock_ticker, date)
upper_band, lower_band = get_bbands(stock_ticker)
plot_bbands(stock_ticker, upper_band, lower_band)
```

<!-- #region -->


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`stocksignals` was created by Ruslan Dimitrov, Robin Dhilon, Peng Zhang, Chenyang Wang. It is licensed under the terms of the MIT license.

## Credits

`stocksignals` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
<!-- #endregion -->
