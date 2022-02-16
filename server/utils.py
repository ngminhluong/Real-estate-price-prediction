import json
import pickle

# define global variables
__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __locations
    global __data_columns
    global __model

    with open('artifacts\\columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open('artifacts\\linear_regression.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())