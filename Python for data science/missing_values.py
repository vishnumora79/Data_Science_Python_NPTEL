# # -*- coding: utf-8 -*-
# """
# Created on Tue Aug 29 18:49:28 2023

# @author: vishn
# """
# #importing pandas library to work with dataframes
import pandas as pd

# #read the csv file 
cars_data = pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])

# #make copies of the dataframe
cars_data2 = cars_data.copy()
cars_data3 = cars_data2.copy()

# #check number of null values are there in each column
print(cars_data2.isna().sum())

# #subsetting the rows that have one or more missing values
# missing = cars_data2[cars_data2.isnull().any(axis = 1)]

print(cars_data2.describe())

# # 1.Imputing missing values of "Age"

cars_data2["Age"].fillna(cars_data2["Age"].mean(),inplace = True)


# # 2.Imputing missing values of "KM"

# cars_data2["KM"].fillna(cars_data2["KM"].median(),inplace = True)

# # 3.Imputing missing values of "HP"

# cars_data2["HP"].fillna(cars_data2["HP"].mean(),inplace = True)

# print(cars_data2.isna().sum())

# print(cars_data2["FuelType"].value_counts())

# # 4.Imputing missing values of "FuelType"

# #print(cars_data2["FuelType"].value_counts().index[0])
# cars_data2["FuelType"].fillna(cars_data2["FuelType"].value_counts().index[0],inplace = True)

# # 5.Imputing missing values of "MetColor"

# print(cars_data2["MetColor"].value_counts())

# cars_data2["MetColor"].fillna(cars_data2["MetColor"].value_counts().index[0],inplace = True)

# print(cars_data2.isnull().sum())

# ------------------------------
# import pandas as pd
# from sklearn.impute import SimpleImputer

# cars_data = pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])

# cars_data2 = cars_data.copy()

# #print(cars_data.isna().sum())

# #print(cars_data2.describe())

# missing = cars_data2[cars_data2.isnull().any(axis=1)]

# #1.Imputing missing values for "Age"
# imputer = SimpleImputer(strategy = "mean")
# Age_imputed = imputer.fit_transform(cars_data2["Age"].values.reshape(-1,1))
# cars_data2["Age"] = Age_imputed
# print(cars_data2.isna().sum())