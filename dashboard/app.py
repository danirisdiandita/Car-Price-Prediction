from flask import Flask
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import requests 


from elements.numerical import numerical_values 
from elements.categorical import categorical_values
from elements.prediction import prediction_values 
from elements.headers import header_values 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.title = "Audi Car Price Prediction"

# current features 
# categorical: model, transmissions, fuelType
# numerical: year, mileage, tax, mpg, engineSize 

app.layout = dbc.Container([
    header_values(), 
    numerical_values(), 
    categorical_values(), 
    prediction_values()
], fluid=True)


@app.callback(
    Output("price-prediction-values", "children"), 
    Output("year-slider-value", "children"), 
    Output("mileage-slider-value", "children"), 
    Output("tax-slider-value", "children"), 
    Output("mpg-slider-value", "children"), 
    Output("engineSize-slider-value", "children"), 
    Output("model-dropdown-value", "children"), 
    Output("fuelType-dropdown-value", "children"), 
    Output("transmission-dropdown-value", "children"), 
    Input("year-slider", "value"), 
    Input("mileage-slider", "value"), 
    Input("tax-slider", "value"), 
    Input("mpg-slider", "value"), 
    Input("engineSize-slider", "value"), 
    Input("model-dropdown", "value"), 
    Input("fuelType-dropdown", "value"), 
    Input("transmission-dropdown", "value")
)
def get_prediction_output(year_value, mileage_value, tax_value, mpg_value, enginesize_value, model_value, fueltype_value, transmission_value):
    input_json = {
        "model": model_value, 
        "year": year_value, 
        "transmissions": transmission_value, 
        "fuelType": fueltype_value, 
        "tax": tax_value, 
        "mpg": mpg_value, 
        "engineSize": enginesize_value, 
        "mileage": mileage_value 
    }

    req = requests.post(url="http://car-prediction:80/predict", json=input_json)
    return 'SEK {0:.2f}'.format(req.json().get("prediction")), str(year_value), str(mileage_value), str(tax_value), str(mpg_value), str(enginesize_value), str(model_value), str(fueltype_value), str(transmission_value)


if __name__ == "__main__": 
    app.server.run(host="0.0.0.0", port=8000, debug=False, threaded=False)