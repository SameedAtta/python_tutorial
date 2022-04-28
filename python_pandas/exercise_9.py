# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 15:01:10 2022

@author: sameed.atta
"""

import pandas as pd
import numpy as np
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan],
'age':[23,45,45]
})
target_age = 45
response = df.query('age == 23')
