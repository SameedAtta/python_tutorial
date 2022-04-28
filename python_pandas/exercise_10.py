# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:48:32 2022

@author: sameed.atta
"""

import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK', 'USA'],
'age':[23,45,45]
})
names_array = ['john','anna']
response = df.query('name in @names_array')
