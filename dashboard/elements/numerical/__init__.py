import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# numerical: year, mileage,  tax, mpg, engineSize 

def numerical_values(): 
    return dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Year Manufactured"), 
                    dcc.Slider(
                        id="year-slider", 
                        min=1997, 
                        max=2020, 
                        value=2017,
                        marks={str(year): str(year) for year in range(1997, 2020+1, 20)}, 
                        step=1, 
                        className="mb-2 ml-2 mt-2"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Car Total MileAge"),
                    dcc.Slider(
                        id="mileage-slider", 
                        min=0, 
                        max=323000, 
                        value=29900,
                        step=100, 
                        className="mb-2 ml-2 mt-2"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Tax Value"), 
                    dcc.Slider(
                        id="tax-slider", 
                        min=0, 
                        max=580, 
                        value=20,
                        step=20, 
                        className="mb-2 ml-2 mt-2"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("MPG"), 
                    dcc.Slider(
                        id="mpg-slider", 
                        min=18, 
                        max=190, 
                        value=67,
                        step=1, 
                        className="mb-2 ml-2 mt-2"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Engine Size"), 
                    dcc.Slider(
                        id="engineSize-slider", 
                        min=0.0, 
                        max=6.3, 
                        value=2.0,
                        step=0.1
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

    ], className="mb-2")