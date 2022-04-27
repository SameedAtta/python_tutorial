# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:48:52 2022

@author: sameed.atta
"""

# Exercise 5
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = " bEautiful"
string1 = string1.lower()
# (string2 will pass unmodified)
string3 = string3.lower()
string4 = string4.strip().lower()
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))