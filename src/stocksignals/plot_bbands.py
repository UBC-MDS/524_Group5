import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.renderers.default = "png"

def plot_bbands(stock_ticker, upper_band, lower_band):
    """
    Plot stock price along with upper and lower Bollinger band
    
    Parameters
    ----------
    stock_ticker : string 
        Ticker of the stock such as 'MSFT'
    upper_band : list
        A list with upper band values of 2 standard deviations above
        specified moving average
    lower_band : list
        A list with lower band values of 2 standard deviations above
        specified moving average
    
    Returns
    --------
    plotly chart
        A chart with stock price along with upper and lower bands
    
    Examples
    --------
    >>> plot_bbands('MSFT', upper_band, lower_band)
    """
    data = pd.read_csv('../../data/'+"MSFT"+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    df = data[['Close']]
    df['upper'] = upper_band
    df['lower'] = lower_band 
    pio.templates.default = "plotly_dark"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, 
                             y=df['lower'] , 
                             name='Lower Band', 
                             line_color='rgba(173,204,255,0.2)'
                            ))
    fig.add_trace(go.Scatter(x=df.index, 
                             y=df['upper'], 
                             name='Upper Band', 
                             fill='tonexty', 
                             fillcolor='rgba(173,204,255,0.2)', 
                             line_color='rgba(173,204,255,0.2)'
                            ))
    fig.add_trace(go.Scatter(x=df.index, 
                             y=df['Close'], 
                             name='Close', 
                             line_color='#636EFA'
                            ))
    fig.show()