
from dash import html

from app import app


def generate_header():
    return html.Div(
        [
            html.Img(
                src=app.get_asset_url('img/images.jfif'),
                className='col-2',
            ),
            html.Div(
                [
                    html.H2(
                        'Dashboard Project',
                        className="d-flex justify-content-center"
                    ),
                    html.H4(
                        'Crypto Currency Price Analysis',
                        className="d-flex justify-content-center"
                    )
                ],

                className='col-8'
            ),
            html.A(
                html.Button(
                    "Learn More",
                    id="learnMore"

                ),
                href="https://coinmarketcap.com/",
                className="col-2"
            )
        ],
        id="header",
        className='row mb-5',
    )