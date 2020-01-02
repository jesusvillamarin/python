# -*- coding: utf-8 -*-

# DOCS about to try and catch that exists https://docs.python.org/3.5/reference/compound_stmts.html#try

my_list = [1,2,3,4,5] # This list just having max 4 index (0,1,2,3,4)

try:
    print(f'Print out the value to index 5, this is wrong: {my_list[5]}')
except IndexError:
    print('The value that you want to get its out of range')
else:
    print('If the value that you want to get is valid, this will be execute')
finally:
    print('finally this will always printed')

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'venezuela': 35,
    'chile': 18
}

while True:
    country = input('Write a country to search: ').lower()
    try:
        print(f'The population of {country} is {countries[country]} million')
    except KeyError:
        print(f'Sorry, we don\'t have the country {country}')