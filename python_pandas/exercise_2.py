# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:15:03 2022

@author: sameed.atta

"""
import pandas as pd

names= ['umer', 'ali', 'usman']
ages =[21,23,25]

data = []


for name, age in zip(names, ages):
    data.append({'name': name, 'age':age})
# Create from lists
# data_dicts = [
# {'name':"john","gender":'male','age':45},
# {'name':"mary", 'gender':"female",'age':19},
# {'name':"peter",'gender':'male', 'age':34}
# ]


df = pd.DataFrame.from_records(data)
