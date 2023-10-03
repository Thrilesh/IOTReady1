from jinja2 import Environment, FileSystemLoader
import json

# Load the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Load the JSON data
with open('data.json', 'r', encoding='utf-8') as json_file:  # Specify encoding
    data = json.load(json_file)

# Render the template with the data
html_output = template.render(data=data)

# Save the rendered HTML to a file
with open('output.html', 'w', encoding='utf-8') as html_file:  # Specify encoding
    html_file.write(html_output)
