import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def prediction_values(): 
    return dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Price Prediction'),
                        html.H2(id="price-prediction-values", children="000")
                    ], style={'textAlign':'center'})
                ]),
            ], width=12)
        ],className='mb-2')