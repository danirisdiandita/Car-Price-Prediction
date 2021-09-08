from flask import Flask
import dash
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from elements.numerical import numerical_values 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server
app.title = "Audi Car Price Prediction"

# current features 
# categorical: model, year, transmissions, fuelType
# numerical: year, mileage, tax, mpg, engineSize 


