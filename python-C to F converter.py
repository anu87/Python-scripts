# -*- coding: utf-8 -*-
"""
Spyder Editor


This is a temporary script file"""
from __future__ import print_function #import functions from future versions of python
print("Hello!")
#Simple Celcius to Fahrenheit converter
# user inputs a temperature in Celcius,
# and it outputs the corresponding 
# Fahrenheit
#
CELSIUS = 100
FAHRENHEIT = CELSIUS * (9/5) +32

print ("Well", CELSIUS, "in CELSIUS is:", FAHRENHEIT, "in FAHRENHEIT!")

CELSIUS = 100
FAHRENHEIT = CELSIUS * (9/5) +32 # write 9.0 instead of 9 because numbers
# and integers are treated as separate if 9/5 is used the results will rounded
#of to 1 instead of 1.8; results will not be 212.8 but only 212 - only in 
#python 2 and lower

# : followed by indented next line shows that next line belongs to the earlier line
# indent is equivalent of { } in other languages
def convert_to_fahrenheit(degrees):
    """Convert the given degrees Celsius into Fahrenheit, and return it."""
    #""" - text with quotation marks following a function is read as a string
    # can be used to define what the fn does - just like #comment but gets
    #stored in the function such that help will show this text
    result = degrees * (9.0/5.0) + 32
    return result
CELCIUS = 100
FAHRENHEIT = convert_to_fahrenheit(CELSIUS) #although it is celsius inside 
# the brackets, since we have already defined convert_to_farenheit() as 
# a fn - python will take whatever input inside () and rename it to degrees
# and run the program

print ("Well", CELSIUS, "in CELSIUS is:", FAHRENHEIT, "in FAHRENHEIT!")


try:
    input = raw_input #take whatever the input (may exist or not) and connect 
    #it to raw input
except NameError:
    pass

def convert_to_fahrenheit(degrees):
    """Convert the given degrees Celsius into Fahrenheit, and return it."""
    result = degrees * (9.0/5.0) + 32
    return result

user_degrees = input("Temp in Celsius:")
CELSIUS = float(user_degrees)
FAHRENHEIT = convert_to_fahrenheit(CELSIUS)

print ("Well", CELSIUS, "in CELSIUS is:", FAHRENHEIT, "in FAHRENHEIT!")








