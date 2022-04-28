# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:10:48 2022

@author: sameed.atta
"""

import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK', 'USA'],
'age':[23,45,45]
})
invalid_array = ['anna']
response=df.query('name not in @invalid_array')