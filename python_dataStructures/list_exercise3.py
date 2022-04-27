# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:56:28 2022

@author: sameed.atta
"""

# Using the append() method to append an item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Insert an item as the second position
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Add the elements of tropical to thislist
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)