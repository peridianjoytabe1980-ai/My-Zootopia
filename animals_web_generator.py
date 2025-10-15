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

    output += f'<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += f'  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    output += f'      <strong>Location:</strong> {locations}<br/>\n'
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'
    output += f'  </p>\n'
    output += f'</li>\n'

new_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(new_html)







