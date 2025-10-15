import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals = load_data("animals_data.json")

for animal in animals:
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    animal_type = animal.get("characteristics", {}).get("type")
    locations = ", ".join(animal.get("locations", []))

    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Locations: {locations}")
    if animal_type:  # Only print if type exists
        print(f"Type: {animal_type}")
    print()
