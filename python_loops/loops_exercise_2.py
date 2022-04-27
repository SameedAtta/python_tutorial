# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:03:15 2022

@author: sameed.atta
"""

its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False # end the while loop
    else:
        print("Enter y or n next time.")
        print("It's not raining anymore.")