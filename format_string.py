def get_address_string(address):
    return 'I am from {country}, {city}, {street}, {house}'.format(**address)

fruits = 'apple'
count = 25

address = {
    'country': 'Russia',
    'city': 'Moscow',
    'street': 'Taganskay',
    'house': '23'
}

address1 = {
    'country': '1123123',
    'city': 'Mos1231312cow',
    'street': 'Tag123123anskay',
    'house': '212312313'
}


print(get_address_string(address))
print(get_address_string(address1))

print('В магазине ' + str(count) + ' ' + fruits)
print('В магазине {0} {1}'.format(fruits, count))

