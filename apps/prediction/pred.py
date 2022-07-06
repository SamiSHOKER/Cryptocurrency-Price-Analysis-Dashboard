from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from app import app
from utils.kpi import generate_kpi, literal_number
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


valid = pd.read_csv(r'C:\Users\sshoker\Desktop\School_files\amse\dashboard\Dashboard_TS\data\valid.csv')
valid = valid.set_index('Unnamed: 0')

performance = pd.read_csv(r'C:\Users\sshoker\Desktop\School_files\amse\dashboard\Dashboard_TS\data\performance.csv')

def create_layout1():
    content1 = html.Div([
        html.H3("Price Prediction Using LSTM Algorithem", style={"textAlign": "center"}),
        html.Hr(),
        html.P("Choose coin of interest:"),
        html.Div(html.Div([
            dcc.Dropdown(id='coin-type', clearable=False,
                        value="BTC-USD",
                        options=[{'label': x, 'value': x} for x in
                                valid["Crypto-USD"].unique()]),
        ],className="two columns"),className="row"),

        html.Div(id='output-div2', children=[]),
    ])
    return content1

@app.callback(Output(component_id='output-div2', component_property="children"),
              Input(component_id="coin-type", component_property="value"),)

def make_graphs1(crypto_chosen2):
    valid1 = valid[valid['Crypto-USD'] == crypto_chosen2]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(valid1['Close']))), y=list(valid1['Close']), name='Closing Price'))
    fig.add_trace(go.Scatter( y=list(valid1['Predictions']), name='Prediction'))
    fig.update_layout(legend_title_text='Legend')
    rmse = performance[performance['Crypto-USD'] == crypto_chosen2]['RMSE'].reset_index(drop = True)[0]
    r_square = performance[performance['Crypto-USD'] == crypto_chosen2]['R_square'].reset_index(drop=True)[0]

    kpi1 = generate_kpi('Root Man Squared Error', literal_number(round(rmse,3)))
    kpi2 = generate_kpi('R_Square', literal_number(round(r_square,3)))



    return [

        html.Div([
            html.Div([dcc.Graph(figure=fig)], className="twelve columns"),
        ], className="row"),
        html.Div(
            html.Div([kpi1, kpi2],
            id="six columns"),className="row")
        ]