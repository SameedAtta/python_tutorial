# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:23:12 2022

@author: sameed.atta
"""

# Get the value of the "model" key
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)
# Get a list of the keys:
x = thisdict.keys()
# Get a list of the values:
x = thisdict.values()
# Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change
# The pop() method removes the item with the specified key name:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")
print(thisdict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)
# The del keyword removes the item with the specified key name
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)
