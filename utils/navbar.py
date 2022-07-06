
import dash_bootstrap_components as dbc
from dash import Input, Output, html

apps = {
    0: {
        'name': 'Overview',
        'id': 'overview'
    },
    1: {
        'name': 'Price Prediction',
        'id': 'prediction'
    }
}


class GenerateTabs:

    def __init__(self, active_tab, apps=apps):
        self.apps = apps
        self.active_tab = active_tab

    def generate_tabs(self):
        tabs = [
            dbc.Tab(label=v['name'], tab_id=v['id'])
            for v in self.apps.values()
        ]
        return dbc.Tabs(
            id='tabs',
            active_tab=self.active_tab,
            children=tabs
        )

    def generate_navbar(self):
        tabs = self.generate_tabs()
        return html.Div([tabs])

