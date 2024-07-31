# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 06:12:59 2023

@author: vishn
"""

# =============================================================================
# CLASSIFYING PERSONAL INCOME
# =============================================================================

 # 1.PACKAGES
#To change the working directory
import os
#To work with dataframes
import pandas as pd
#To perform numerical operations
import numpy as np
#To visualize data
import seaborn as sns
#To split the data
from sklearn.model_selection import train_test_split
#Importing library for Logistic Regression
from sklearn.linear_model import LogisticRegression
#Importing performance metrics- accuracy_score & confusion_matrix
from sklearn.metrics import accuracy_score,confusion_matrix

# =============================================================================
# To change the working directory 
# Here to avoid escape character error we can use any one of following methods
#Double backslashs
# os.chdir("E:\\Python-py\\NPTEL\\DATA-SCIENCE\\classification-problem")
#Raw String
# os.chdir(r"E:\Python-py\NPTEL\DATA-SCIENCE\classification-problem")
#Forward slashes
# os.chdir("E:/Python-py/NPTEL/DATA-SCIENCE/classification-problem")
# =============================================================================

os.chdir("E:\\Python-py\\NPTEL\\DATA-SCIENCE\\classification-problem")

# =============================================================================
#   # 2.IMPORTING DATA
# =============================================================================

data_income = pd.read_csv("income.csv")
print(data_income)
#Creating a copy of original data
data = data_income.copy()

#Exploratory data analysis:
    # 1.Getting to know the data
    # 2.Data Preprocessing (Missing values)
    # 3.Cross tables and data visualization
    
# =============================================================================
# Getting to know the data    
# =============================================================================
    
#To check the variables data type
print(data.info())
#Check number of missing values
print("Data columns with missing values:\n",data.isna().sum())
#Summary of numerical variables
summary_num = data.describe()
print(summary_num)
#Summary  of categorial variables
summary_category = data.describe(include = "O")
print(summary_category)
# Frequency of each category
data["JobType"].value_counts()
data["occupation"].value_counts()
# Checking for unique classes
np.unique(data["JobType"])
np.unique(data["occupation"])
# there exists " ?" special symbol instead of nan
data = pd.read_csv("income.csv",na_values = [' ?'])

# =============================================================================
# DATA PREPROCESSING 
# =============================================================================

data.isnull().sum()
missing = data[data.isnull().any(axis = 1)]

#Drop null values
data2 = data.dropna(axis = 0)
#Cross tabulation and data visualization
gender = pd.crosstab(index = data2["gender"],columns = "count",normalize=True)
# gender vs salary-status
gender_salstat = pd.crosstab(index=data2["gender"],columns = data2["SalStat"],normalize = "index",margins = True)
# Frequency distribution of salary status
SalStat = sns.countplot(data2["SalStat"])
# Histogram of Age
sns.distplot(data2["age"],bins = 10,kde = False)
# Box plot of age vs salary status
sns.boxplot(x = "SalStat",y = "age",data = data2)
data2.groupby("SalStat")["age"].mean()

# =============================================================================
# NOTE: Since machine learning models cannot work with categorical data directly so,we can convert into numbers
# =============================================================================
data2["SalStat"] = data2["SalStat"].map({" less than or equal to 50,000":0," greater than 50,000":1})

new_data = pd.get_dummies(data2,drop_first=True)

columns = list(new_data.columns)
features = list(set(columns) - set(["SalStat"]))
print(features)
len(features)
x = new_data[features].values
print(x)
y = new_data["SalStat"].values
print(y)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.3)
# print(train_y)
model = LogisticRegression()

model.fit(train_x,train_y)

prediction = model.predict(test_x)


confusion_matrix = confusion_matrix(test_y,prediction)
print(confusion_matrix)

accuracy = accuracy_score(test_y,prediction)
print(accuracy)

cols = ["gender","nativecountry","race"]

new_data = data2.drop(cols,axis = 1)

new_data1 = pd.get_dummies(new_data,drop_first = True)

columns = list(new_data1.columns)
print(columns)
features = list(set(columns) - set(["SalStat"]))
print(features)
len(features)
x = new_data1[features].values
y = new_data1["SalStat"].values
print(x)
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size = 0.3)
print(test_y)
model = LogisticRegression()

model.fit(train_x,train_y)

prediction = model.predict(test_x)

confusion_matrix = confusion_matrix(test_y,prediction)
print(confusion_matrix)

accuracy = accuracy_score(test_y,prediction)
print(accuracy)

print("misclassified samples are:",(test_y != prediction).sum())


# =============================================================================
# KNN CLASSIFIER
# =============================================================================

from sklearn.neighbors import KNeighborsClassifier

import matplotlib.pyplot as plt

model = KNeighborsClassifier(n_neighbors = 5)

model.fit(train_x,train_y)

KNN_prediction = model.predict(test_x)

confusion_matrix = confusion_matrix(test_y,prediction)
print(confusion_matrix)

accuracy = accuracy_score(test_y,prediction)
print(accuracy)

print("misclassified samples are:",(test_y != prediction).sum())

misclassified_sample = []
for i in range(1,20):
    model = KNeighborsClassifier(n_neighbors = i)
    model.fit(train_x,train_y)
    prediction = model.predict(test_x)
    misclassified_sample.append((test_y != prediction).sum())

print(misclassified_sample)
