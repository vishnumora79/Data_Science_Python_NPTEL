# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:45:11 2023

@author: vishn
"""

import os
import numpy as np
import pandas as pd

os.chdir("E:\Python-py")

data_csv = pd.read_csv("Toyota.csv",na_values=["??","????"])
print(data_csv)

# print(data_csv['Price'][1])



# data_csv.insert(10,"Price_Class" , "")

# print(data_csv)


# for i in range(len(data_csv)):
#     if(data_csv['Price'][i] <= 8450):
#         data_csv['Price_Class'][i] = 'Low'
#     elif(data_csv['Price'][i] > 11940):    
#         data_csv['Price_Class'][i] = 'High'
#     else:
#         data_csv['Price_Class'][i] = 'Medium'

# print(data_csv)


# print(data_csv['Price'][1])


# data_csv.insert(10,"Price_Class","")
# print(data_csv)

# print(data_csv.dtypes)

# for i in range(0,len(data_csv['Price'])):
#     if (data_csv['Price'][i] <= 8450):
#         data_csv['Price_Class'][i] = 'Low'
#     elif (data_csv['Price'][i] <= 11950):    
#         data_csv['Price_Class'][i] = 'High'
#     else:
#         data_csv['Price_Class'][i] = 'Medium'
# 
#

# FUNCTION EXAMPLE

#data_csv.insert(11,"Age-converted",0)
#data_csv.insert(12,"km_per_mont


# print(data_csv)



def convert(val_1,val_2):
    x1 = val_1 / 12
    x2 = val_2 / val_1
    return [x1,x2]
data_csv["Age_Converted"],data_csv["Km_Per_Month"] = convert(data_csv["Age"],data_csv["KM"])
data_csv["Age_Converted"] = round(data_csv["Age_Converted"],2)
data_csv["Km_Per_Month"] = round(data_csv["Km_Per_Month"],2)
print(data_csv)

# ====
# data_csv1 = data_csv.copy()
# tab = pd.crosstab(index=data_csv1["Automatic"],columns=data_csv1["FuelType"],dropna=True)
# print(tab)
# print(tab.memory_usage())
# print(tab.size)
# 
# =============================================================================
data_csv.insert(10,"Condition","")
for i in range(0,len(data_csv["Km_Per_Month"])):
    if(data_csv["Km_Per_Month"][i] <= 300):
        data_csv["Condition"][i] = "Good"
    elif(data_csv["Km_Per_Month"][i] >= 1800):
        data_csv["Condition"][i] = "Very bad"
    else:
        data_csv["Condition"][i] = "Not bad"
print(data_csv)     
  
        