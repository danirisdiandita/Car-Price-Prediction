import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

# categorical: model,  transmissions, fuelType

from mappings import fuelType_keys, transmission_keys, model_keys 

def categorical_values(): 
    return dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Car Model'),
                        dcc.Dropdown(
                            id='model-dropdown',
                            options=[{'label': i, 'value': i} for i in model_keys],
                            value='A6'
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Fuel Type'),
                        dcc.Dropdown(
                            id='fuelType-dropdown',
                            options=[{'label': i, 'value': i} for i in fuelType_keys],
                            value='Petrol'
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Transmission'),
                        dcc.Dropdown(
                            id='transmission-dropdown',
                            options=[{'label': i, 'value': i} for i in transmission_keys],
                            value='Automatic'
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3)
        ],className='mb-2')