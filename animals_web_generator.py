import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

for animal in load_data("animals.json.py"):
  print(animal)


animals_data = load_data('animals_data.json.py')
