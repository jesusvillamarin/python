# -*- coding: utf-8 -*-

# List and dictionary comprehensions is a syntantic sugar

# LIST
my_list = []
for number in range(1, 31): # Loop for 1 to 30
    if number % 2 == 0:
        my_list.append(number)

print(f'The even list is: {my_list}')

# How do the same with syntatic sugar (List Comprehension)
even_list = [num for num in range(1,31) if num % 2 == 0]
print(even_list)

# DICTIONARY
squared_numbers = {}
for number in range(1, 6): 
    squared_numbers[number] = number**2

print(f'The squared numbers is: {squared_numbers}')

# Doing the same with Syntactic sugar (Dictionary Comprehension)

squared_numbers_ss = {number: number**2 for number in range(1,6)}
print(f'The squared numbers with Syntactic sugar is: {squared_numbers_ss}')
