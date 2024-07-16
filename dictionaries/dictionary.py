# dictionary - A changeale, unordered collection of unique key value pairs
    # - they are fast because they use hashing

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'Kenya': 'Nairobi',
    'South Africa': 'cape Town',
    'Russia': 'Moscow'
}

capitals.update({ 'Germany': 'Berlin' })
capitals.update({ 'China': 'Beijing' })
capitals.update({ 'Germany': 'Munic' })
capitals.pop({ 'China' })

print(capitals['Russia']) # not safe for accessing values
print(capitals.get('Kenya'))
print(capitals.keys()) # keys only
print(capitals.values()) # values only
print(capitals.items()) # all

for key, value in capitals.items():
    print(key, value)