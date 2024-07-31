# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:16:39 2023

@author: vishn
"""

import pandas as pd

import numpy as np

import os

os.chdir("E:\Python-py")

data_csv = pd.read_csv("Lottery_dataset.csv")

print(data_csv)

# =============================================================================
# new_data_csv_1 = data_csv.copy(deep = False)
# 
# #print(new_data_csv_1)
# 
# #print(new_data_csv_1.index)
# 
# #print(new_data_csv_1.columns)
# 
# #print(new_data_csv_1.size)
# 
# #print(new_data_csv_1.shape)
# 
# print("dimension:",new_data_csv_1.ndim)
# 
# #print(new_data_csv_1.memory_usage())
# 
# #print(new_data_csv_1.head(7))
# 
# #print(new_data_csv_1.tail(7))
# 
# #print(new_data_csv_1.at[4,'Mega Ball'])
# 
# #print(new_data_csv_1.iat[5,1])
# 
# #print(new_data_csv_1.loc[4,'Mega Ball'])
# 
# print("data type of each columns:" , new_data_csv_1.dtypes)
# 
# #print(new_data_csv_1.get_dtypes_counts())
# 
# # =============================================================================
# # print(new_data_csv_1.select_dtypes(include = ["int64"]))
# # print(new_data_csv_1.select_dtypes(include = ["float64",'object']))
# # 
# # print(new_data_csv_1.info())
# # 
# # print(np.unique(new_data_csv_1["Multiplier"]))
# # print(np.unique(new_data_csv_1["Mega Ball"]))
# # print(np.unique(new_data_csv_1["Winning Numbers"]))
# # print(np.unique(new_data_csv_1['Draw Date']))
# # 
# # =============================================================================
# #new_data_csv_1['Winning Numbers'] = new_data_csv_1['Winning Numbers'].astype("int64")
# 
# #print(new_data_csv_1.dtypes["Winning Numbers"])
# 
# #print(new_data_csv_1['Winning Numbers'].nbytes)
# #print(new_data_csv_1['Winning Numbers'].astype("category").nbytes)
# #print(new_data_csv_1["Draw Date"].astype("category").ntypes)
# print("Total number of bytes:",data_csv['Draw Date'].nbytes)
# print("total number of category bytes:",data_csv['Draw Date'].astype("category").nbytes)
# #new_data_csv_1['Winning Numbers'] = new_data_csv_1['Winning Numbers'].replace('44 47 49 69 75' , [44,47,49,69,75])
# 
# print(new_data_csv_1.isnull().sum())
# 
# 
# =============================================================================

