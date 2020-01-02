# -*- coding: utf-8 -*-

# Where consult about assign multi values to multi variables (https://note.nkmk.me/en/python-multi-variables-values/)
# Rounding decimals  https://realpython.com/python-rounding/

def find_number(number, array, *args): 
    if args == (): low_index, high_index = 0, len(array)-1
    else: low_index, high_index = args
    
    if low_index > high_index:
        return -1

    mid_index = int((low_index + high_index) / 2)

    if array[mid_index] == number:
        return mid_index
    elif array[mid_index] > number:
        return find_number(number, array, low_index, mid_index-1)
    else:        
        return find_number(number, array, mid_index +1 , high_index)


if __name__ == '__main__':
    print('Program that uses binary search to find a number in an array')
    array_length = int(input('How much number you will insert?: '))
    array = list()
    for i in range(array_length):
        number = int(input('Write a number: '))
        array.append(number)
    array.sort()
    print(f'Ok, this is your array sorted {array}')
    number =  int(input('Write the number to find: '))
    print('Ok, wait a moment')
    print(f'You number its found on position: {find_number(number, array)+1}')