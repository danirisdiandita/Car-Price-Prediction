from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class CarPrice(BaseModel):
    model: str 
    year: int
    transmissions: str
    mileage: int
    fuelType: str
    tax: int
    mpg: float
    engineSize: float