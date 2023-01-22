# Stocksignals

Calculate buy/sell signal indicators for a stock!


## Authors:
    - Ruslan Dimitrov
    - Robin Dhillon
    - Peng Zhang
    - Chenyang Wang

This data science project is created for DSCI 524 (Collaborative Software Development); a course in the Master of Data Science program at the University of British Columbia.

## Introduction

The goal of this project is to develop a package which can be used as a starting point for identifying stock buy/sell signals. Stock investing is a complex process which requires ongoing efforts and there is no one formula or indicator that works all the time. There exists extensive research on how to identify opportunities and profit from stocks. Methodologies for evaluating financial instruments range widely. An investor can utilize macroeconomic research, fundamental analysis, news, analyst reports, or technical analysis. In all those approaches numerical analysis is the underlying common theme.

In this project, the team aims to evaluate three key technical indicators that can be used to evaluate where the stock price is relative to its historic performance. These indicators use only the stock's historic price and are by no means an exhaustive approach to investing. These indicators are:

- 200-day price moving average
- 10 vs 20-day price moving average
- 20-day Bollinger bands

Typically when the market and stocks in particular are trading below 200-day moving average, they are considered in a down trend.  When they trade above the 200-day moving average stocks are considered in an uptrend.  The 10-20 day indicator, indicates short term price trend reversals, and can be utilized to trade stocks on a short term basis.  Finally, the Bollinger bands indicate whether a stock price is above or below two standard deviations from its 20 day average price.  Bbands can be used as indicator for short term overbought/oversold stocks.

<!-- #region -->
## Package details
The package consists of 6 functions:
- `get_data`: The function downloads all available historic price data for a selected stock and saves it. It utilizes the `yfinance` python package to automate the process. 
- `moving_average`: The function (inside `calc_moving_average.py` module) calculates a moving average, i.e. the average stock closing price over a specified period, which is passed as argument `size` in the function call. It uses the data saved via `get_data`.
- `plot_ma_200days`: The function plots the 200-day moving average together with the stock price for a specified period, say the past 200 trading days.  It uses the output from the function `calc_moving_avg` to plot the chart.
- `plot_ma_10_20`: The function plots the 10 and 20-day moving average together with the stock price for a specified period, say the past 200 trading days. It uses the output from function `move_ave_10_20` to plot the chart.
- `get_bbands`: The function (inside `bbands.py` module) calculates the 20 day Bollinger bands for the existing period of the data and returns a Pandas DataFrame with the respective upper and lower band. It uses data saved via `get_data`.
- `plot_bbands`: The function plots upper and lower Bollinger bands together with the stock closing price for over the past 200 days. It uses the output from function `bbands` to plot the chart.


## Python ecosystem

There are multiple packages related to utilizing finance data. For example, past projects in DSCI524 have explored various transformations to help analyzing stocks like this one: https://github.com/UBC-MDS/stockAnalyzer.  Other packages like this one https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis have explored volatility analysis.  

Our aim is to explore specific technical analysis indicators and streamline the process by providing a hands-on package which can be used in daily stock analysis. Furthermore, this package will help streamline the process in order to help automation of the basics of stock screening.

<!-- #endregion -->

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
get_data.get_data(stock_ticker)
calc_moving_average.moving_average(stock_ticker, size)
plot_ma_10_20.plot_ma_10_20(stock_ticker)
plot_ma_200days.plot_ma_200days(stock_ticker)
bbands.get_bbands(stock_ticker)
plot_bbands.plot_bbands(stock_ticker)
```

<!-- #region -->


## Contributing

Interested in contributing? Check out the [contributing](CONTRIBUTING.md) guidelines. Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`stocksignals` was created by Ruslan Dimitrov, Robin Dhilon, Peng Zhang, Chenyang Wang. It is licensed under the terms of the MIT license.

## Credits

`stocksignals` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
<!-- #endregion -->
