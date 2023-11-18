import json

def generate():
    data = {"items": []}
    for i in range(100000):  # Adjust the range as needed to reach the desired file size
        data["items"].append({"id": i, "value": "Some example text or data"})

    with open('../../data/large_file.json', 'w') as json_file:
        json.dump(data, json_file)