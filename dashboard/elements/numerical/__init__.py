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
                    html.H1(id="year-slider-value", children="2017"), 
                    dcc.Slider(
                        id="year-slider", 
                        min=1997, 
                        max=2020, 
                        value=2017,
                        marks={str(year): str(year) for year in range(1997, 2020+1, 5)}, 
                        step=1, 
                        className="mb-2 ml-2 mt-2 h-100"
                    ), 
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Car Total MileAge"),
                    html.H1(id="mileage-slider-value", children="29900"), 
                    dcc.Slider(
                        id="mileage-slider", 
                        min=0, 
                        max=323000, 
                        value=29900,
                        marks={str(mileage): str(mileage) for mileage in range(0, 323000, 65000)},
                        step=100, 
                        className="mb-2 ml-2 mt-2 h-100"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Tax Value"), 
                    html.H1(id="tax-slider-value", children="20"), 
                    dcc.Slider(
                        id="tax-slider", 
                        min=0, 
                        max=580, 
                        value=20,
                        marks={str(tax): str(tax) for tax in range(0,580,120)},
                        step=20, 
                        className="mb-2 ml-2 mt-2 h-100"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("MPG"), 
                    html.H1(id="mpg-slider-value", children="67"), 
                    dcc.Slider(
                        id="mpg-slider", 
                        min=18, 
                        max=190, 
                        value=67,
                        marks={str(mpg): str(mpg) for mpg in range(18,190,35)},
                        step=1, 
                        className="mb-2 ml-2 mt-2 h-100"
                    )
                ], style={"textAlign": "center"})
            ])
        ], width=3), 

    ], className="mb-2")