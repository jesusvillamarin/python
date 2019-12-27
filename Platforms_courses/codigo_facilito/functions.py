def testing1_sum_numbers(number1, number2, number3 = 3):
    return number1 + number2 + number3

def testing2_sum_numbers(number1, *, number2,number3):
    return number1 + number2 + number3

print(testing1_sum_numbers(1,2,3))
print(testing1_sum_numbers(1, number2=1, number3= 3))

# Is obligatory define the args with name when the args are after the asterisk
print(testing2_sum_numbers(1,number2=2,number3=3)) # This will run correctly ✔
try:
    print(testing2_sum_numbers(1,2,3)) # This will produce an error when executing 🤔🤔
except:
    print('''(Line 13) This will produce an error when executing 🤔(face)🤔(face)''', end=" ")
    print(''' Don't worry and keep enjoying''')

# In Python3.8 a new features has been added
# When you create a function with args and you put '/' on the args 👇
# you must pass the arguments by position before the slash '/'

def function_testing_with_slash(number1, number2, /, number3, number4):
    return number1 + number2 + number3 + number4

try:
    print(function_testing_with_slash(number2=2, number1=1, number3=3, number=4))
except:
    print('''(Line 26) 👆 (hand up) It Will produce an error when executing because the first two args must be position args and NOT named args''')
 #  👆 It Will produce an error when executing because the first two args must be position args and NOT named args


print(function_testing_with_slash(1,2, number3=3, number4=4)) # This will run correctly ✔
print(function_testing_with_slash(1,2, 3, 4)) # This will run correctly ✔


# Function with multiple values on any variable 
def asterisk_arg(*args):
    return "The all pass value are: ", args

# This is a beautiful method to receive multiples values on any arg
print(asterisk_arg(100, {"Nombre": "Jesús", 1: 22}, [{"Paises Visitados": ["México", "Guatemala", "Colombia"]}] ))


# Function with multiple values on any variable with names
def kwargs_function(**kwargs):
    print(kwargs.items())
    return "The all pass value are: ", kwargs

print(kwargs_function(a=1, b=22, c=33, d=4, dictionary={"nombre": "Jesus"}))


