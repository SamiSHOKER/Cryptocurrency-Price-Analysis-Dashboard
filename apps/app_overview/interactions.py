
from dash import html
from dash import dcc

import pandas as pd

df = pd.read_csv(r'C:\Users\sshoker\Desktop\School_files\amse\dashboard\Dashboard_TS\data\crypto.csv')

start_date = pd.to_datetime(df['Date']).dt.date.min()
end_date = pd.to_datetime(df['Date']).dt.date.max()


def get_interactions():
    return html.Div(
        [
            html.P(
                'Filter by date:',
                className="control_label"
            ),
            dcc.DatePickerRange(
                id='date_picker',
                start_date=str(start_date),
                end_date=str(end_date),
                className="dcc_control"
            ),
            html.P(
                'Choose Cryptocurrency:',
                className="control_label"
            ),
            dcc.Dropdown(
                id='coin',
                options=states_options,
                value=[],
                multi=True,
                className="dcc_control"
            ),
            html.Button(
                id='app_overview_state',
                n_clicks=0,
                className="btn btn-primary position-relative mt-5",
                children="Go"
            )
        ],
        className="pretty_container col-4"
    )