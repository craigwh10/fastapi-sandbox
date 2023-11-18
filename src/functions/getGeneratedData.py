import json

def getGeneratedData():
    with open('../../data/large_file.json', 'r') as json_file:
        return json.load(json_file)