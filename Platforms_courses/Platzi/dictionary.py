# -*- coding: utf-8 -*-
# DOCS ABOUT DICTIONARIES
#    https://developer.rhino3d.com/guides/rhinopython/python-dictionaries/
#    https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# HOW DECLARE A DICTIONARY
person_dict = {}
# OR -----------------------------------------------------------
person_dict = dict()

# HOW INITIALIZE A DICTIONARY
person_dict = {"Name": "Jesús", "Surname": "Villamarin", "Age": 22}
# OR -----------------------------------------------------------
person_dict = dict([("Name", "Jesús"), ("Surname", "Villamarín"), ("Age", 22)])

# HOW ITERATE EACH KEY OF A DICTIONARY OR PRINT ALL KEYS
print(person_dict.keys()) # Print all keys'
for key in person_dict.keys(): # Iterate each key of dictionary
    print(f'The key is: {key} ')
    
# OR -----------------------------------------------------------
print("Second method to print keys")
for key in person_dict: # Iterate each key of dictionary
    print(f'The key is: {key} ')



# HOW ITERATE EACH VALUE OF A DICTIONARY OR PRINT ALL VALUES
print(person_dict.values()) # Print all values'
for value in person_dict.values(): # Iterate each value of dictionary
    print(f'The value is: {value} ')

# HOW ITERATE EACH PAIR (KEY, VALUE) OF A DICTIONARY OR PRINT ALL KEYS AND VALUES
print(person_dict.items()) # Print all keys and values
for key, value in person_dict.items(): # Iterate each key and value of dictionary
    print(f'The value for {key} is: {value}')


# HOW TO ASSIGN VALUES TO A DICTIONARY AFTER INITIALIZED
person_dict['new_field'] = 'it\'s a test ✔'
person_dict[0] = "The key zero is valid"
person_dict[22] = 'The key it\'s my age'
print(person_dict)
