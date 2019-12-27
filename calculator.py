'''
    Autor: JESÚS AURIOL VILLAMARÍN ORTIZ
    DATE: 28/11/2019
    DESCRIPTION: HOW TO USE PYTHON AS CALCULATOR, COURSERA VIDEO 1.1.4
'''

y = 2
x = 4
print(y+x)
y=7
print(y+x)

# ======== THIS A TEST 
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot