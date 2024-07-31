# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:53:54 2023

@author: vishn
"""

import os
import numpy as np
import pandas as pd

data = pd.read_csv("Toyota.csv",index_col = 0,na_values=["??","????"])
print(data)
# =============================================================================
# #Memory decrease by converting from OBJECT TO CATEGORY
# print(data['FuelType'].nbytes)
# print(data["FuelType"].astype("category").nbytes)
# 
# #COUNTING MISSING VALUES
# print(data.isnull().sum())
# print(data["Price"].isnull().sum())
# 
# #TO FIND UNIQUE VALUES
# 
# print(np.unique(data["Price"]))
# 
# #to select variables based on datatype
# 
# print(data.select_dtypes(exclude = ["object"]))
# 
# =============================================================================
# =============================================================================
#FREQUENCY TABLES
# fr = pd.crosstab(index = data['FuelType'],columns='counts',dropna=True)
# print(fr)
# #TWO-WAY-TABLES
# fr = pd.crosstab(index = data["FuelType"],columns=data["Automatic"],dropna=True)
# print(fr)


# =============================================================================
# =============================================================================
# # JOINT PROBABILITY
# jp = pd.crosstab(index = data["Automatic"], columns=data["FuelType"],dropna=True,normalize=True)
# print(jp)
#MARGINAL PROBABILITY
# mp = pd.crosstab(index=data["Automatic"],columns=data["FuelType"],dropna=True,normalize=True,margins=True)
# print(mp)
# =============================================================================


# =============================================================================
#CONDITIONAL PROBABILITY
# cp_rows = pd.crosstab(index=data["Automatic"],columns = data["FuelType"],dropna=True,normalize="index")# =============================================================================
# print(cp_rows)
# cp_columns = pd.crosstab(index = data["Automatic"],columns=data["FuelType"],dropna=True,normalize="columns")
# print(cp_columns)
# =============================================================================
# #Correlation
# #1.by default "nan" values will be excluded
# #2.to exclude categorial variables
numerical_data = data.select_dtypes(exclude=["object"])
# #3.for numerical data correlation "pearson" method is used
correlation = numerical_data.corr()
print(correlation)
# =============================================================================




















