import json
import pickle
import numpy as np

__towns = []
__districts = []
__data_columns = None
__model = None

def get_town_names():
    return __towns 

def get_district_names():
    return __districts

def get_estimated_price(bed, bath, land, sqft, town, district):
    try:
        loc_index_Town = __data_columns.index("town_" + town.lower())
        loc_index_District = __data_columns.index("district_" + district.lower())
    except:
        loc_index_Town = -1
        loc_index_District = -1

    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = land
    x[3] = sqft
    if loc_index_District >= 0:
        x[loc_index_District] = 1
    if loc_index_Town >= 0:
        x[loc_index_Town] = 1

    return round(__model.predict([x])[0],2)

def load_saved_artifacts():
    print("loading saved artifacts...")
    global __data_columns
    global __towns
    global __districts
    global __model

    with open(r"F:\ML_tutorials\Project1.Real_state_price_predictor\server\Artifacts\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        for town in __data_columns[4:-22]:
            __towns.append(town.split("_")[1])
        for district in __data_columns[-21:]:
            __districts.append(district.split('_')[1])
    
    with open(r"F:\ML_tutorials\Project1.Real_state_price_predictor\server\Artifacts\Sri_Lankan_homePrices.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Saved artifacts are loaded!")


if __name__ == '__main__':
    load_saved_artifacts()
    print(__towns)