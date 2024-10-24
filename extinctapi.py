from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

extinct_animals = [
    {"name": "Dodo", "species": "Raphus cucullatus", "extinct_year": 1662, "location": "Mauritius"},
    {"name": "Passenger Pigeon", "species": "Ectopistes migratorius", "extinct_year": 1914, "location": "North America"},
    {"name": "Tasmanian Tiger", "species": "Thylacinus cynocephalus", "extinct_year": 1936, "location": "Australia"},
    {"name": "Great Auk", "species": "Pinguinus impennis", "extinct_year": 1844, "location": "North Atlantic"},
    {"name": "Baiji (Yangtze River Dolphin)", "species": "Lipotes vexillifer", "extinct_year": 2006, "location": "Yangtze River, China"},
    {"name": "Pinta Island Tortoise", "species": "Chelonoidis abingdonii", "extinct_year": 2012, "location": "Galápagos Islands"},
    {"name": "Pyrenean Ibex", "species": "Capra pyrenaica pyrenaica", "extinct_year": 2000, "location": "Pyrenees Mountains, Spain"},
    {"name": "Western Black Rhinoceros", "species": "Diceros bicornis longipes", "extinct_year": 2011, "location": "Western Africa"},
    {"name": "Steller's Sea Cow", "species": "Hydrodamalis gigas", "extinct_year": 1768, "location": "Bering Sea"},
    {"name": "Carolina Parakeet", "species": "Conuropsis carolinensis", "extinct_year": 1939, "location": "United States"},
]


@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(extinct_animals)

if __name__ == "__main__":
    app.run(debug=True)
