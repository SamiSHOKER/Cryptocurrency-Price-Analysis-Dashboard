
from dash import dash_table

import pandas as pd
import plotly.graph_objects as go


def generate_table_fig(df):
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )


def generate_hbar_fig(
        labels: list = [],
        data: pd.DataFrame = pd.DataFrame(),
        barmode: str = 'group',
        height: int = 250,
    ):

    barmodes = ['group', 'stack']
    if barmode not in barmodes:
        raise ValueError("Invalid sim type. Expected one of: %s" % barmodes)

    bars = [
        go.Bar(
            x=labels,
            y=data[col].tolist()
        )
        for col in data.columns
    ]
    fig = go.Figure(bars)
    fig.update_layout(
        height=height,
        barmode=barmode,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig


def generate_pie_fig(
        labels: list = [],
        data: list = [],
        hole: float = 0.8,
        height: int = 250,
    ):

    pie = go.Pie(labels=labels, values=data, hole=hole)
    fig = go.Figure(data=[pie])
    fig.update_layout(
        height=height,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig