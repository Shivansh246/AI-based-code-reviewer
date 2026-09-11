import json
from jsonschema import validate

with open("schemas/vulnerability.json") as file:
    schema = json.load(file)

with open("schemas/example_static.json") as file:
    finding = json.load(file)

validate(instance=finding, schema=schema)

print("Finding is valid!")  