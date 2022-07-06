from dash import dcc
from dash import html
from dash import Input, Output
from apps.app_overview import views as app_overview_views
from apps.prediction import pred as app_pred_views
from utils.header import generate_header

from app import app

header = generate_header()


app.layout = html.Div([
    header,
    dcc.Tabs(id="tabs-example-graph", value='tab-1-overview-graph', children=[
        dcc.Tab(label='overview', value='tab-1-overview-graph'),
        dcc.Tab(label='prediction', value='tab-2-prediction-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')

])


@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))

def render_content(tab):
    if tab == 'tab-1-overview-graph':
        return app_overview_views.create_layout(),

    elif tab == 'tab-2-prediction-graph':
        return app_pred_views.create_layout1()

if __name__ == '__main__':
    app.run_server(debug=True)
