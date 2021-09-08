import json 

# reading the data mapping from the file
with open("/app/mappings/model_mapping.json") as f: 
    model_mapping = json.load(f)
    model_mapping = {val:key for key, val in model_mapping.items()} # reversed 

# transmissions mapping
with open('/app/mappings/transmission_mapping.json') as f:
    transmission_mapping = json.load(f)
    transmission_mapping = {val:key for key, val in transmission_mapping.items()} # reversed 

# fuel type mapping
with open('/app/mappings/fuelType_mapping.json') as f:
    fuelType_mapping = json.load(f)
    fuelType_mapping = {val:key for key, val in fuelType_mapping.items()} # reversed