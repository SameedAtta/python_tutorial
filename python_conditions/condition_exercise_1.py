# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:30:51 2022

@author: sameed.atta
"""

#If statement:
a = 33
b = 200
if b > a:
print("b is greater than a")
#If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
# The elif keyword is pythons way of saying "if the previous conditions were not true,
# then try this condition".
a = 33
b = 33
if b > a:
print("b is greater than a")
elif a == b:
print("a and b are equal")
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
print("b is greater than a")
elif a == b:
print("a and b are equal")
else:
print("a is greater than b")
