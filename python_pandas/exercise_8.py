# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:55:13 2022

@author: sameed.atta
"""
import numpy as np
import pandas as pd
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan]
})
df.query("country == 'USA'")