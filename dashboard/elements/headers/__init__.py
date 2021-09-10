import dash_bootstrap_components as dbc
import dash_core_components as dcc
from datetime import date 
import dash_html_components as html

def header_values(): 
    return dbc.Row([
        dbc.Col([
            dbc.CardBody([
                html.H1("Audi Car Prediction Dashboard"), 
                html.H2("R^2 = 0.956, Root Mean Square Error = 21237.7")
            ], style={"textAlign": "center"})
        ], width=10), 
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='./assets/logos/INFIDEA DATA PLATFORM-3-01-01.png') # 150px by 45px
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                    dbc.CardLink("Visit Our Site", target="_blank",
                                 href="https://infidea.id"
                    )
                ])
            ]),
        ], width=2)
    ], className="mb-2 mt-2")