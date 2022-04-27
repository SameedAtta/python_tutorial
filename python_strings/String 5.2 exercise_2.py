# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 15:02:04 2022

@author: sameed.atta
"""

# Exercise 2
# Replace every occurrence of the character `"s"`
# with the character `"x"`
phrase = "Somebody said something to Samantha."
phrase = phrase.replace("s", "x")
print(phrase)
# NOTE: This leaves the capital "S" unchanged, so the
# output will be "Somebody xaid xomething to Samantha."