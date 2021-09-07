# import uvicorn
from fastapi import FastAPI
from CarPrices import CarPrice
import pickle
from mappings import (
    model_mapping, 
    transmission_mapping, 
    fuelType_mapping
)

app = FastAPI()
pickle_in = open("model.pkl","rb")
regressor=pickle.load(pickle_in)

scalerfile = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))

@app.get('/')
def index():
    return {'message': 'This is our Car Prediction API'}

@app.post('/predict')
def predict_carprice(data:CarPrice):
    data = data.dict()

    # getting all features 
    model = model_mapping.get(data["model"])
    year= data['year']
    transmissions = transmission_mapping.get(data["transmissions"])
    mileage= data['mileage']
    fuelType = fuelType_mapping.get(data["fuelType"])
    tax= data['tax']
    mpg= data['mpg']
    engineSize= data['engineSize']
    scaler.clip = False
    test_scaled_set = scaler.transform([[model, year, transmissions, mileage,
                                        fuelType, tax, mpg, engineSize]])
    
    prediction = regressor.predict(test_scaled_set)
    return {
        'prediction': prediction[0]
    }

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)