# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:48:06 2023

@author: vishn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data = pd.read_csv("Toyota.csv",index_col=0,na_values=["??","????"])

cars_data.dropna(axis = 0,inplace = True)
#print(cars_data)

#Scatter plot 
sns.set(style="darkgrid")
#sns.regplot(x = "Age" ,y = "Price", data = cars_data,fit_reg=False,marker="." )

#To include another variable into scatter plot
#sns.lmplot(x = "Age",y = "Price",data = cars_data,hue="FuelType" ,legend=True,palette="Set2",markers=".")


#HISTOGRAM

#sns.distplot(x = "Age",data = cars_data ,bins=5)
#without KERNEL DENSITY ESTIMATE (kde = False)

#BAR PLOT -- frequency distribution of catrgorial variable

#sns.countplot(x = "FuelType", data = cars_data)
#sns.countplot(x = "FuelType",data = cars_data,hue = "Automatic")

#BOX & WHISKERS PLOT

#sns.boxplot(y = "Price", data = cars_data)
#sns.boxplot(x = "FuelType", y = "Price",data = cars_data)
#sns.boxplot(x = cars_data["FuelType"],y = cars_data["Price"],hue = "Automatic",data = cars_data)


#SPLITTING THE WINDOW FOR TWO PLOTS

# f,(ax_blox,ax_hist) = plt.subplots(2,gridspec_kw={"height_ratios":(.15,0.85)})
# sns.boxplot(cars_data["Price"],ax = ax_blox)
# sns.distplot(cars_data["Price"],ax = ax_hist,kde=False,bins = 5)

#PAIRWISE PLOTS

sns.pairplot(cars_data,kind = "scatter",hue = "FuelType")
