groceries = {
    'fruits': [],
    'vegetables': [],
}
groceries['fruits'].append('apple')
print(groceries)
fruits = groceries['fruits']
fruits.append('tomato')
print(groceries)

try:
    groceries['yee']
except Exception as e:
    print(e)

with_default = groceries.get('dairy', [])
print(with_default)

suffixes = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'YobaB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB', 'YobiB'],
}
print(suffixes[1024])
print(suffixes[1000][2])

dumb_dict = {
    ('fruits', 'vegetables'): []
}
print(dumb_dict[('fruits', 'vegetables')])
