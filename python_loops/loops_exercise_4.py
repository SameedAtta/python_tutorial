# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:13:49 2022

@author: sameed.atta
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
print(x)
for x in range(2, 30, 3):
    print(x)
for x in range(6):
    print(x)
else:
    print("Finally finished!")