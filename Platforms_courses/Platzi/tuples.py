# -*- coding: utf-8 -*-

'''
    NOTE: 
        * The tuple are inmutable
        * If a tuple are initialized with one element, this should end with comma symbol ",". E.g: my_tuple = (1,).
'''

# HOW DECLARE A TUPLE
my_tuple = (1,2,3,4)
# OR 
my_tuple = 1,2,3,4

# WE CAN'T ASSIGN A VALUE OF AN TUPLE BY INDEX
try:
    my_tuple[0] = 1 # THIS CANNOT BE DONE
except:
    print('Line break. (Line 16)')
# ANY ALTERNATIVE TO CHANGE A VALUE OF ANY TUPLE BY INDEX 
my_tuple = (1,10,4,5,2)
print(my_tuple)
list_from_tuple = list(my_tuple)
list_from_tuple[1] = 2
list_from_tuple[4] = 10
my_tuple = tuple(list_from_tuple)
print(my_tuple)


def extract_unique_letters(repeated_letters):
    unique_letters = list()
    for letter in repeated_letters:
        if letter not in unique_letters:
            unique_letters.append(letter)

    return unique_letters

def select_letter_no_repeated(letter_with_counter):
    selected_letter = ''
    for tuple_letter in letter_with_counter:
        if tuple_letter[1] == 1:
            selected_letter += tuple_letter[0]
    return 'none' if selected_letter is '' else selected_letter

def identify_letter_no_repeated(repeated_letters):
    unique_letters = extract_unique_letters(repeated_letters)
    for index, letter in enumerate(unique_letters):
        repeated_letter_counter = 0
        for repeated_letter in repeated_letters:
            if letter is repeated_letter:
                repeated_letter_counter += 1
        unique_letters[index] = (letter, repeated_letter_counter)

    return select_letter_no_repeated(unique_letters)



if __name__ == '__main__':
    print('Program that extracts the non-repeated letter')
    repeated_letters = input('Write the set of letters: ')
    print(f'The non-repeated letter is: {identify_letter_no_repeated(repeated_letters)}')




