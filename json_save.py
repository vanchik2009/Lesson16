import json
person = {
    'name': 'Max',
    'age': 10,
    'phones': ['9111', '738333']
}
result = json.dumps(person)
print(result)
print(type(result))