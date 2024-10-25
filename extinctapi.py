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
    {"name": "Saber-toothed Cat", "species": "Smilodon fatalis", "extinct_year": 10000, "location": "North America"},
    {"name": "Woolly Mammoth", "species": "Mammuthus primigenius", "extinct_year": 1650, "location": "North America"},
    {"name": "Moa", "species": "Dinornithiformes", "extinct_year": 1440, "location": "New Zealand"},
    {"name": "Terror Bird", "species": "Phorusrhacidae", "extinct_year": "1.8 million years ago", "location": "South America"},
    {"name": "Irish Elk", "species": "Megaloceros giganteus", "extinct_year": 7000, "location": "Europe and Asia"},
    {"name": "Stag Moose", "species": "Cervalces scotti", "extinct_year": 10000, "location": "North America"},
    {"name": "Caspian Tiger", "species": "Panthera tigris virgata", "extinct_year": 1970, "location": "Caucasus region"},
    {"name": "Bubal Hartebeest", "species": "Alcelaphus buselaphus buselaphus", "extinct_year": 1923, "location": "North Africa"},
    {"name": "Tapanuli Orangutan", "species": "Pongo tapanuliensis", "extinct_year": 2017, "location": "Indonesia"},
    {"name": "Guam Kingfisher", "species": "Todiramphus cinnamominus", "extinct_year": 1987, "location": "Guam"},
    {"name": "Rudd's Lark", "species": "Heteromirafra ruddi", "extinct_year": 1987, "location": "South Africa"},
    {"name": "Labrador Duck", "species": "Camptorhynchus labradorius", "extinct_year": 1875, "location": "North America"},
    {"name": "Bluebuck", "species": "Hippotragus leucophaeus", "extinct_year": 1790, "location": "South Africa"},
    {"name": "Zanzibar Leopard", "species": "Panthera pardus adersii", "extinct_year": 1996, "location": "Zanzibar"},
    {"name": "Javan Tiger", "species": "Panthera tigris sondaica", "extinct_year": 1972, "location": "Java, Indonesia"},
    {"name": "Pleistocene Horse", "species": "Equus ferus", "extinct_year": 10000, "location": "North America"},
    {"name": "North Island Moa", "species": "Megalapteryx didinus", "extinct_year": 1500, "location": "New Zealand"},
    {"name": "Dwarf Woolly Mammoth", "species": "Mammuthus primigenius", "extinct_year": 4000, "location": "Wrangel Island"},
    {"name": "Haas's Frog", "species": "Rana haasi", "extinct_year": 1980, "location": "Haiti"},
    {"name": "Spix's Macaw", "species": "Cyanopsitta spixii", "extinct_year": 2000, "location": "Brazil"},
    {"name": "Caribbean Monk Seal", "species": "Neomonachus tropicalis", "extinct_year": 1952, "location": "Caribbean Sea"},
    {"name": "Golden Toad", "species": "Incilius periglenes", "extinct_year": 1989, "location": "Costa Rica"},
    {"name": "Huntington's Frog", "species": "Rana capito", "extinct_year": 2003, "location": "United States"},
    {"name": "Plesiosaur", "species": "Plesiosauria", "extinct_year": "65 million years ago", "location": "Marine environments"},
    {"name": "Woolly Rhinoceros", "species": "Coelodonta antiquitatis", "extinct_year": 1650, "location": "Eurasia"},
    {"name": "Giant Ground Sloth", "species": "Megatherium americanum", "extinct_year": 10000, "location": "South America"},
    {"name": "Megalodon", "species": "Carcharocles megalodon", "extinct_year": "3.6 million years ago", "location": "Marine environments"},
    {"name": "Diprotodon", "species": "Diprotodon optatum", "extinct_year": 46000, "location": "Australia"},
    {"name": "Cave Bear", "species": "Ursus spelaeus", "extinct_year": 24000, "location": "Europe"},
    {"name": "Short-faced Bear", "species": "Arctodus simus", "extinct_year": 11000, "location": "North America"},
    {"name": "Megatherium", "species": "Megatherium americanum", "extinct_year": 10000, "location": "South America"},
    {"name": "Thylacine", "species": "Thylacinus cynocephalus", "extinct_year": 1936, "location": "Tasmania"},
    {"name": "Elephant Bird", "species": "Aepyornis maximus", "extinct_year": 1662, "location": "Madagascar"},
    {"name": "Barbary Lion", "species": "Panthera leo leo", "extinct_year": 1960, "location": "North Africa"},
    {"name": "Mauritius Blue Pigeon", "species": "Alectroenas nitidissimus", "extinct_year": 1830, "location": "Mauritius"},
    {"name": "Dusky Seaside Sparrow", "species": "Ammospiza nigrescens", "extinct_year": 1987, "location": "Florida, USA"},
    {"name": "Pied Tamarin", "species": "Saguinus bicolor", "extinct_year": 2000, "location": "Brazil"},
    {"name": "Rhinoceros Auklet", "species": "Cerorhinca monocerata", "extinct_year": 1850, "location": "California"},
    {"name": "Cory's Shearwater", "species": "Calonectris diomedea", "extinct_year": 1940, "location": "Tropical Oceans"},
    {"name": "Spoon-billed Sandpiper", "species": "Calidris pygmaea", "extinct_year": 2019, "location": "Eastern Asia"},
    {"name": "Yellow-billed Cuckoo", "species": "Coccyzus americanus", "extinct_year": 1970, "location": "North America"},
    {"name": "Takahe", "species": "Porphyrio hochstetteri", "extinct_year": 1898, "location": "New Zealand"},
    {"name": "Passenger Pigeon", "species": "Ectopistes migratorius", "extinct_year": 1914, "location": "North America"},
    {"name": "Ivory-billed Woodpecker", "species": "Campephilus principalis", "extinct_year": 1944, "location": "North America"},
    {"name": "Javan Rhinoceros", "species": "Rhinoceros sondaicus", "extinct_year": 1990, "location": "Java"},
    {"name": "Red Wolf", "species": "Canis rufus", "extinct_year": 1970, "location": "North America"},
    {"name": "Spix's Macaw", "species": "Cyanopsitta spixii", "extinct_year": 2000, "location": "Brazil"},
    {"name": "Alaskan Wood Frog", "species": "Lithobates sylvaticus", "extinct_year": 1990, "location": "Alaska"},
    {"name": "Thylacine", "species": "Thylacinus cynocephalus", "extinct_year": 1936, "location": "Tasmania"}
]


@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(extinct_animals)

if __name__ == "__main__":
    app.run(debug=True)
