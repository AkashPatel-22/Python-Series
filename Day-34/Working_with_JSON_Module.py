# JSON(JavaScript Object Notations).
# -is a lightweight data format used to exchange data between programs,
# APIs, website, etc. JSON format is very similar to python dictionaries.
# python JSON module allows you to read,write,encode and decode JSON

# Importing the Module
# ex - import json

# Converting Python to JSON
# - we use dumps() tp convert python objects into JSON string

import json

data = {"name": "akash","age":23, "marks": [85,90,92]}

json_string = json.dumps(data)
print(json_string)


# converting JSON to python
# - we use loads() to convert json dtring to python dictionary.

json_data = '{"name": "akash","age":23, "marks": [85,90,92]}'
python_obj = json.loads(json_data)
print(python_obj["name"])

