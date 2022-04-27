# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:59:36 2022

@author: sameed.atta
"""

# Sort the list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Sort the list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# Use the extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
