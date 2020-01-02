# -*- coding: utf-8 -*-

# Set's is related to "set theory"
# In sets cannot have repeated values
# "Set" has three main methods (union, intersection, difference)

# How declare a set
s = set([1,2,3,5])
t = set([4,5,6,2])

# Using method union
print(s.union(t))

# Using method intersection
print(s.intersection(t))

# Using method difference
print(s.difference(t))


# From two lists, get values no repeated and distinct
# DOCS https://stackoverflow.com/questions/28444561/get-only-unique-elements-from-two-lists-python
x = [1,2,3,4]
f = [1,11,22,33,44,3,4]
l = list(set(x).symmetric_difference(set(f)))
print(l)

# WAY TO GET THE HEAD AND TAIL FROM A LIST
# DOCS https://stackoverflow.com/questions/10532473/head-and-tail-in-one-line

# cabeza get the first value from the list and cola get the rest of the list
cabeza, *cola = [0,1,2,3,4,5,6,7]
print(cabeza) # 0
type(cabeza) #<class 'int'>
print(cola) # [1.2.3.4.5.6.7]
type(cola) # <class 'list'>

