# -+- coding: utf-8 -+-

'''
    # TO DO

    *  READ ABOUT SORTING ALGORITHMS IN THIS LINK https://www.geeksforgeeks.org/sorting-algorithms/

'''

# This class is an attempt to sort the array without reading about "Sorting Algorithms"

def sort_array(array):
    print(f'Unordered array {array}')
    i = 0
    while i < len(array)-1:
        print(i)
        if array[i] > array[i+1]:
            temp_value = array[i+1]
            array[i+1] = array[i]
            array[i] = temp_value
            i+=1

        print(array[i]< array[i-1])
        print(array[i-1])

        if array[i] < array[i-1]:
            temp_value = array[i-1]
            array[i-1] = array[i]
            array[i] = temp_value
            i -= 1
        
    print(f'Ordered array {array}')
    
if __name__ == '__main__':
    array_length = int(input('Write the quantity of number to insert: '))
    array = []
    for i in range(array_length):
        array.append(int(input('Write a number: ')))
    sort_array(array)