# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:30:07 2023

@author: vishn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_cars = pd.read_csv("W3Example.csv",index_col=0)

df_cocoa = pd.read_csv("cocoa.csv")

df_hotel_bookings = pd.read_csv("hotel_bookings.csv")

df_mtcars = pd.read_csv("mtcars.csv")

# print(df_cars)
# print(df_cocoa)
# print(df_hotel_bookings)
print(df_mtcars)

# print(df_cars.loc[:,["Type"]])
# print(df_cars.describe())

# max_locations = pd.value_counts(df_cocoa["Company Location"])
# print(max_locations)

# print(df_cocoa.info()

# maxi = max(df_cocoa["Rating"])
# print(maxi)

# data_hotel_us = df_hotel_bookings[df_hotel_bookings.reservation_status == "No-Show"]
# print(data_hotel_us)

#CHECK IT - ANSWER WRONG
cancel = pd.value_counts(df_hotel_bookings.arrival_date_month[df_hotel_bookings.arrival_date_year == 2017 and df_hotel_bookings.is_canceled == 0])
print(cancel)

# plt.scatter(df_mtcars["mpg"],df_mtcars["wt"],marker="*",label =  "points")
# plt.title("mpg VS wt")
# plt.xlabel("mpg")
# plt.ylabel("wt")
# plt.legend()
