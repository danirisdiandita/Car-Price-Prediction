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
                        html.H6("Engine Size"), 
                        html.H1(id="engineSize-slider-value", children="2.0"), 
                        dcc.Slider(
                            id="engineSize-slider", 
                            min=0.0, 
                            max=6.3, 
                            value=2.0,
                            marks={str(engine): str(engine) for engine in range(0,7,1)},
                            step=0.1, 
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={"textAlign": "center"})
                ])
            ], width=3), 
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Car Model'),
                        html.H1(id="model-dropdown-value", children="A6"), 
                        dcc.Dropdown(
                            id='model-dropdown',
                            options=[{'label': i, 'value': i} for i in model_keys],
                            value='A6', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Fuel Type'),
                        html.H1(id="fuelType-dropdown-value", children="Petrol"), 
                        dcc.Dropdown(
                            id='fuelType-dropdown',
                            options=[{'label': i, 'value': i} for i in fuelType_keys],
                            value='Petrol', 
                            className="mb-2 ml-2 mt-2 h-100" 
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H6('Transmission'),
                        html.H1(id="transmission-dropdown-value", children="Automatic"), 
                        dcc.Dropdown(
                            id='transmission-dropdown',
                            options=[{'label': i, 'value': i} for i in transmission_keys],
                            value='Automatic', 
                            className="mb-2 ml-2 mt-2 h-100"
                        )
                    ], style={'textAlign':'center'})
                ]),
            ], width=3)
        ],className='mb-2')