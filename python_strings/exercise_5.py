# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:59:46 2022

@author: sameed.atta
"""

# Exercise 5
weight = 0.2
animal = "newt"
# Concatenate a number and a string in one print statement
print(str(weight) + " kg is the weight of the " + animal + ".")
# Use format() to print a number and a string inside of another string
print("{} kg is the weight of the {}.".format(weight, animal))
# Use formatted string literal (f-string) to reference objects inside a string
print(f"{weight} kg is the weight of the {animal}.")
