# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:48:37 2022

@author: sameed.atta
"""
'''make gravitational function'''
mass1 = float(input("First mass: "))
mass2 = float(input("Second mass: "))
r = float(input("Distance between the objects: "))
G = 6.673*(10**-11)
force =(G*mass1*mass2)/(r**2)
print("The gravitational force is:", round(force, 5),"N")