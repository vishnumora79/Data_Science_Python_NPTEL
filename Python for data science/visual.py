# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 19:07:38 2023

@author: vishn
"""

import os

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

data = pd.read_csv("Toyota.csv",na_values=["??","????"])

data.dropna(axis = 0,inplace = True)
# data.info()

#SCATTER-PLOT
# plt.title('Scatter plot of AGE vs PRICE')
# plt.xlabel("age(months)")
# plt.ylabel("price(rupees)")
# plt.scatter(data["Age"], data["Price"], c = 'red',label="datapoints")
# plt.legend()
# plt.xticks()
#HISTOGRAM
# =============================================================================
# plt.title("Histogram of KiloMeters(KM)")
# plt.xlabel("Kilometer")
# plt.ylabel("Frequency")
# plt.hist(data['KM'],
#          color="green",
#          edgecolor = "white",
#          bins = 5)
# 
# =============================================================================

# =============================================================================
# #BAR-PLOT
# plt.title("bar-plot of PETROL vs Frequency")
# plt.xlabel("FuelType")
# plt.ylabel("Frequency")
# fueltype = ("petrol","diesel","CNG") 
# count = pd.value_counts(data["FuelType"])
# index = np.arange(len(fueltype))
# plt.bar(index,count,color = ["red","blue","cyan"])
# plt.xticks(index,fueltype,rotation = 90)
# =============================================================================

# font1 = {"family":"serif",'color' : "green",'size' : "20"}
# font2 = {"family" : "impact","color":"blue","size":"15"}
# plt.xlabel("numbers",fontdict=font1)
# plt.ylabel("numbers",fontdict = font2)
# plt.title("Drawing a line")
# xpoints = np.array([1,8,5,10])
# ypoints = np.array([3,10,3,1])
# plt.plot(xpoints,ypoints,marker = "o",ls = '--',color = "b",ms = 30,mec = 'b',mfc = "g",lw = 5)
# 1.mfc stands for MARKER FACE COLOR
# 2.mec stands for MARKER EDGE COLOR
# 3.marker used to specity type of marker used
# 4.ms stands for MARKER SIZE
# 5.ls stands for LINESTYLE
# 6.lw stands for LINEWIDTH
# 7.fontdict used to apply font to the 'title','xlabel','ylabel'


# plt.figure()
# # plt.scatter(data["Age"],data["Price"],color = "blue")
# plt.scatter(data["Weight"],data["Price"],color = "green")
# plt.title("Scatter plot of Age Vs Price")
# plt.xlabel("Age")
# plt.ylabel("Price")
# plt.show()

