# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:19:53 2022

@author: sameed.atta
"""

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for upper, lower in zip(uppercase, lowercase):
    print(upper, lower)
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for index, letterpair in enumerate(zip(uppercase, lowercase), start=1):
    upper, lower = letterpair
print(index, upper, lower)