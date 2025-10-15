import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


with open("animals_template.html", "r") as file:
    template_content = file.read()

animals = load_data("animals_data.json")

output = ""


for animal in animals:
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    animal_type = animal.get("characteristics", {}).get("type")
    locations = ", ".join(animal.get("locations", []))

    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    if animal_type:  # Only print if type exists
        output += f"Type: {animal_type}\n"
    output += '</li>'


new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(new_html)







