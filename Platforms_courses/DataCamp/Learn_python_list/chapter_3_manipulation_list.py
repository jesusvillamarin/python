# INFORMATION ======================================================================
'''
    You should copy list with reference or without reference
'''

print("*" * 10, " With Reference ", "*" * 10)
person_names = ["Jesús", "Humberto", "Sara", "Ronald"]
students = person_names

del person_names[3]

# If you print person_names and students, you will see that both array are afected
print("person_names: ", person_names)
print("students: ", students)

# The output will be ["Jesús", "Humberto", "Sara"]

print("*" * 10, " Without Reference ", "*" * 10)

# Method one ========================================================================
person_names = ["Jesús", "Humberto", "Sara", "Ronald"]
students = list(person_names)

del person_names[3]

# If you print person_names and students, you will see that only person_names array are afected
print("person_names: ", person_names)
print("students: ", students)

# Method two ========================================================================
person_names = ["Jesús", "Humberto", "Sara", "Ronald"]
students = person_names[:]

del person_names[3]

# If you print person_names and students, you will see that only person_names array are afected
print("person_names: ", person_names)
print("students: ", students)


# INFORMATION ======================================================================
'''
    # Replace list elements
    Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

    Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

    x = ["a", "b", "c", "d"]
    x[1] = "r"
    x[2:] = ["s", "t"]
'''

# TEST BY EXPLICATION ==============================================================
x = ["a","b","c", "d"]
x[1] = "R"
print(x)
x[2:] = ["DO", "RE", "MI", " FA"]
print(x)


# ACTIVITY ========================================================================
'''
    * Update the area of the bathroom area to be 10.50 square meters instead of 9.50.
    * Make the areas list more trendy! Change "living room" to "chill zone".
'''

# CODE ===========================================================================

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50
# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)


# INFORMATION ==============================================================
'''
    Extend a list
    If you can change elements in a list, you sure want to be able to add elements to it,right? You can use the + operator:

    x = ["a", "b", "c", "d"]
    y = x + ["e", "f"]
'''

# TEST BY EXPLICATION ==============================================================

inmediate_family = ["Sara", "Humberto", "Teodolinda", "Marcos"]
general_family = ["Auriol", "Ronald", "Rouneth"] + inmediate_family


# ACTIVITY =========================================================================

'''
    You just won the lottery, awesome! You decide to build a poolhouse and a garage. Can you add the information to the areas list?

    * Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.

    * Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.

'''


# CODE ==============================================================================

# Create the areas list and make some changes
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)

areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

# SIMPLIFY CODE
areas += ["poolhouse", 24.5]
areas += ["garage", 15.45]
print(areas)

# INFORMATION 
'''
    Delete list elements
    Finally, you can also remove elements from your list. You can do this with the del statement:
'''
x = ["a", "b", "c", "d"]
del(x[1])
'''
    Pay attention here: as soon as you remove an element from a list, the indexes of the elements that come after the deleted element all change!

    The updated and extended version of areas that you've built in the previous exercises is coded below. You can copy and paste this into the IPython Shell to play around with the result.
'''

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

'''
    -- QUESTION 
    There was a mistake! The amount you won with the lottery is not that big after all and it looks like the poolhouse isn't going to happen. You decide to remove the corresponding string and float from the areas list.

    The ; sign is used to place commands on the same line. The following two code chunks are equivalent:
'''
del(x[1]); del(x[-1])

# ANSWER TO QUESTION
del(areas[-4:-2])

