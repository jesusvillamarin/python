# -*- coding: utf-8 -*-

# DOCS TO ABOUT ALL ENUMERATES https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/


# How create a list 
my_list = list() # we can also create a list like this my_list = []
print(my_list) 

# How to add an elemento to the list
my_list.append('first element')
print(my_list[0])

# We can also use this form
my_list2 = [22, 30, 60]
my_list += my_list2
print(my_list)

# How to delete an element from the list
my_list.pop()
print(my_list)

# we can also use the following
del my_list[0]
print(my_list)
