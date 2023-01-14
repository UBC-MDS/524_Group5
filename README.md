# Stocksignals

Calculate buy/sell signal indicators for a stock!


## Contributors:
- Ruslan Dimitrov
- Robin Dhillon
- Peng Zhang
- Chenyang Wang


## Introduction

The goal of this project is to develop a package which can be used as a starting point for identifying stock buy/sell signals. Stock investing is a complex process which requires ongoing efforts and there is no one formula or indicator that works all the time.  There exists extensive research on how to identify opportunities and profit from stocks.  Methodologies for evaluating financial instruments range widely.  An investor can utilize macroeconomic research, fundamental analysis, news, analyst reports, or technical analysis.  In all those approaches numerical analysis is the underlying common theme.

In this project the team aims to evaluate three key technical indicators that can be used to evaluate where the stock price is relative to its historic performance.  These indicators use only the stock's historic price and are by no means an exhaustive approach to investing.  These indicator are:

- 200-day price moving average
- 10 vs 20-day price moving average
- 20-day Bollinger bands

Typically when the market and stocks in particular are trading below 200-day moving average, they are considered in a down trend.  When they trade above the 200-day moving average stocks are considered in an uptrend.  The 10-20 day indicator, indicates short term price trend reversals, and can be utilized to trade stocks on a short term basis.  Finally, the Bollinger bands indicate whether a stock price is above or below two standard deviations from its 20 day average price.  Bbands can be used as indicator for short term overbought/oversold stocks.


## Package details
The package consists of 7 functions:
- Download historic price data for a particular stock
- Calculate 200-day moving average of the daily closing price
- Plot 200-day moving average together with the stock price
- Calculate 10 and 20-day moving averages of the daily closing price
- Plot the 10 and 20-day moving averages together with the stock closing price
- Calculate 20 day Bollinger bands
- Plot stock price together with Bollinger bands

There are multiple packages related to utilizing finance data.  For example past projects in DSCI524 have focused explored various transformation to help analyzing stocks like this one: https://github.com/UBC-MDS/stockAnalyzer.  Other packages like this one https://github.com/UBC-MDS/Stock-Price-Trend-Volatility-Analysis have explored volatility analysis.  

What we aim to do is explore specific technical analysis indicators and streamline the process thus both providing a hands-on package which can be used in daily stock analysis and streamline the process in order to help automation of the basics of stock screening.



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
