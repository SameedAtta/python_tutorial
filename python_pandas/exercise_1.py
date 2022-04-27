# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:15:03 2022

@author: sameed.atta
"""

# Create from lists
import pandas as pd
data = {
'names':['john','mary','peter','gary','anne'],
'ages':[33,22,45,23,12]
}
df = pd.DataFrame(data)
print(df)