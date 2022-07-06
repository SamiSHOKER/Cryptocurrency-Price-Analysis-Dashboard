
from dash import html


def literal_number(n):
    return '{:,}'.format(n).replace(',', ' ')


def generate_kpi(label, value):
    return html.Div(
        [
            html.P(label),
            html.H6(value, className="info_text")
        ],
        className="pretty_container"
    )