# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:12:35 2022

@author: sameed.atta
"""

import pandas as pd
import numpy as np
df = pd.DataFrame({
'name':['john','david','anna'],
'country':['USA','UK',np.nan]
})
response=df.query('country.isnull()', engine='python')