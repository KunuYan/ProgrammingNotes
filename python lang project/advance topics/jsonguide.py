import json

"""
people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "6137328617",
            "emails": ["kanma.aa@gmail.com", "niowa@outlook.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "687444617",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
"""

'''
# load a json string into a python object
data = json.loads(people_string)
for person in data['people']:
    print(person['name'])
    del person['phone']

# dump pythonobject into json string
new_string = json.dumps(data, indent=2, sort_keys=True)
# use indent to format it in a way that is easy to read, and use sort_keys to sort keys in alphabetic order
print(new_string)
'''

# load a json file into a python object
with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])
    del state['area_codes']
# dump python object into a json file
with open('new_states', 'w') as f:
    json.dump(data, f, indent=2)