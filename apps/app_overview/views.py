
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from app import app
import plotly.express as px
import pandas as pd

df = pd.read_csv(r'C:\Users\sshoker\Desktop\School_files\amse\dashboard\Dashboard_TS\data\crypto.csv')
df['Date'] = df['Date'].astype('datetime64[ns]')

def create_layout():
    content = html.Div([

        html.P("Choose coin of interest:"),
        html.Div(html.Div([
            dcc.Dropdown(id='coin-type', clearable=False,
                        value="BTC-USD",
                        options=[{'label': x, 'value': x} for x in
                                df["Crypto-USD"].unique()]),
        ],className="two columns"),className="row"),

        html.Div(id="output-div", children=[]),
    ])
    return content


@app.callback(Output(component_id="output-div", component_property="children"),
              Input(component_id="coin-type", component_property="value"),
)
def make_graphs(crypto_chosen):
    # Closing price with range selector button
    df_line = df[df["Crypto-USD"]==crypto_chosen]
    fig_price = px.line(df_line, x='Date', y='Close', title='Closing price with Range Slider and Selectors')
    fig_price.update_traces(line_color='purple')
    fig_price.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )


    fig_volume = px.line(df_line, x='Date', y='Volume', title='Trading Volume with Range Slider and Selectors')
    fig_volume.update_traces(line_color='firebrick')
    fig_volume.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    df_return = df[df["Crypto-USD"] == crypto_chosen]
    df_return['daily_return'] = (df_return['Close']/ df_return['Close'].shift(1)) -1
    df_return = df_return.dropna()
    fig_return = px.line(df_return, x='Date', y='daily_return', title='Daily Return ')
    fig_return.update_traces(line_color='lime')
    fig_return.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])

        )
    )
    fig_hist = px.histogram(df_return, x='daily_return', marginal="rug" )

    return [
        html.H3("Price and Volume History", style={"textAlign": "center"}),
        html.Hr(),
        html.Div([
            html.Div([dcc.Graph(figure=fig_price)], className="twelve columns"),
            html.Div([dcc.Graph(figure=fig_volume)], className="twelve columns"),
        ], className="row"),
        html.H3("Return History", style={"textAlign": "center"}),
        html.Hr(),
        html.Div([
            html.Div([dcc.Graph(figure=fig_return)], className="twelve columns"),
            html.Div([dcc.Graph(figure=fig_hist)], className="twelve columns"),
        ], className="row"),

    ]


