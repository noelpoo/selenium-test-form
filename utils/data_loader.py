import os
import json

def load_json_data(filename):
    filepath = os.path.join("data", filename)
    with open(filepath, "r") as file:
        return json.load(file)
