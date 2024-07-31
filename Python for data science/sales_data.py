# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:51:24 2023

@author: vishn
"""
#import libraries
import numpy as np
import pandas as pd

#import data
products = ["Product-A","Product-B","Product-C","Product-D"]
base_prices = [10,15,20,25]
number_of_sales = [45,23,67,33]

#calculate revenue,totalcost and profit for each product
revenue = sum(base_prices[i] * number_of_sales[i] for i in range(len(products)))
total_cost = sum(5 * number_of_sales[i] for i in range(len(products)))
profit = revenue - total_cost

#create a dataframe to store dataframe
sales_data = pd.DataFrame({
     "Products" : products,
     "Base Price" : base_prices,
     "Number of Sales":number_of_sales
    })

#calculate revenue and profit from dataframe
sales_data["Revenue"] = sales_data["Base Price"] * sales_data["Number of Sales"]
sales_data["Total Cost"] = sales_data["Number of Sales"] * 5
sales_data["Profit"] = sales_data["Revenue"] - sales_data["Total Cost"]

#print data
print(sales_data)