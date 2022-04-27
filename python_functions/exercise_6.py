# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:00:06 2022

@author: sameed.atta
"""

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
for x in [-1, 0, 1]:
    print(sign(x))