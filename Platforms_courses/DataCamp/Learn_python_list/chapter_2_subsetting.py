# INFORMATION ===============================================================================================
'''
    Subset and conquer
    Subsetting Python lists is a piece of cake. Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.

    x = ["a", "b", "c", "d"]
    x[1]
    x[-3] # same result!

    Remember the areas list from before, containing both strings and floats? Its definition is already in the script. Can you add the correct code to do some Python subsetting?
'''

# ACTIVITY ===============================================================================================
'''
    * Print out the second element from the areas list (it has the value 11.25).
    * Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
    * Select the number representing the area of the living room (20.0) and print it out.
'''

# CODE ===============================================================================================
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])


# INFORMATION TWO (2) ===============================================================================================
'''
    Subset and calculate
    After you've extracted values from a list, you can use them to perform additional calculations. Take this example, where the second and fourth element of a list x are extracted. The strings that result are pasted together using the + operator:

    x = ["a", "b", "c", "d"]
    print(x[1] + x[3])
'''
# ACTIVITY ===============================================================================================

'''
   * Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that        contains the sum of the area of the kitchen and the area of the bedroom.
   * Print the new variable eat_sleep_area.
'''

# CODE ===============================================================================================
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)


# INFORMATION  ===============================================================================================
'''
    Slicing and dicing
    Selecting single values from a list is just one part of the story. It's also possible to slice your list, which means selecting multiple elements from your list. Use the following syntax:

    my_list[start:end]
    The start index will be included, while the end index is not.

    The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:

    x = ["a", "b", "c", "d"]
    x[1:3]
    The elements with index 1 and 2 are included, while the element with index 3 is not.
'''

# ACTIVITY ===============================================================================================
'''
    * Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
    * Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
    * Print both downstairs and upstairs using print().
'''

# CODE ===============================================================================================

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[:6]

# Use slicing to create upstairs
upstairs = areas[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
'''
    Subsetting lists of lists
    You saw before that a Python list can contain practically anything; even other lists! To subset lists of lists, you can use the same technique as before: square brackets. Try out the commands in the following code sample in the IPython Shell:
'''
# CODE TO EXECUTE ===============================================================================================
x = [["a", "b", "c"],
     ["d", "e", "f"],
     ["g", "h", "i"]]
x[2][0]
x[2][:2]

# x[2] results in a list, that you can subset again by adding additional square brackets.

# ACTIVITY ======================================================================================================
#What will x[-1][1] return? x, the list of lists that you created before, is already defined for you in the workspace. You can experiment with it in the IPython Shell.

result = x[-1][1]
print(result) # THE OUTPUT IS "i"