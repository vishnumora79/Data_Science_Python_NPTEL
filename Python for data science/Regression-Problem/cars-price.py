# =============================================================================
# #IMPORT REQUIRED LIBRARIES
# =============================================================================
import os
import pandas as pd
import numpy as np
import seaborn as sns

#To set dimensions for the plot
sns.set(rc = {'figure.figsize':(11.7,8.27)})

#change the working directory
os.chdir(r"E:\Python-py\NPTEL\DATA-SCIENCE\Regression-Problem")

#reading data from file
cars_data = pd.read_csv("cars_sampled.csv")

#Copy the data
cars = cars_data.copy()

#Getting some information
cars.info()

#Summary of the data
cars.describe()
#To set float values to 3 decimals and to show all columns in describe()
pd.set_option("display.float_format",lambda x : "%.3f" % x)
pd.set_option("display.max_columns",50)

cars.describe()

col = ['name','dateCrawled','lastSeen','dateCreated','postalCode']
#To drop the columns 
cars = cars.drop(col,axis = 1)
#To drop duplicate values
cars.drop_duplicates(keep = 'first',inplace = True)

#To find the No of null values
cars.isna().sum()

#Variable yearOfRegistration
yearwise_count = cars.yearOfRegistration.value_counts().sort_index()
sum(cars.yearOfRegistration > 2018)
sum(cars.yearOfRegistration < 1950)
sns.regplot(x = 'yearOfRegistration',y = 'price',scatter=True,fit_reg=False,data = cars)

#Variable Price
price_count = cars.price.value_counts().sort_index()
sum(cars.price > 150000)
sum(cars.price < 100)
sns.distplot(cars.price)
sns.boxplot(cars.price)

#Variable powerPS
power_count = cars.powerPS.value_counts().sort_index()
sum(cars.powerPS > 500)
sum(cars.powerPS<20)
sns.distplot(cars.powerPS)
sns.boxplot(cars.powerPS)
sns.regplot(x = 'powerPS',y = 'price',data = cars,scatter = True,fit_reg = False)

# =============================================================================
# Working range of data
# =============================================================================

cars = cars[(cars.yearOfRegistration <= 2018) &
            (cars.yearOfRegistration >= 1950) &
            (cars.price >= 100) &
            (cars.price <= 150000) &
            (cars.powerPS >= 10) & 
            (cars.powerPS <= 500)
    ]
#6700 records are dropped
#Further to simplify variable reduction
#Combining yearofregistration and monthofregistration to Age


#Creating new variable Age by adding year of registration and month of registration 
cars.monthOfRegistration /= 12
cars['Age'] = (2018 - cars.yearOfRegistration) + cars.monthOfRegistration
cars.Age = round(cars.Age,2)

cars.Age.describe()

#Droping yerofregistration and monthofregistration to reduce redundancy
cars = cars.drop(['yearOfRegistration','monthOfRegistration'],axis = 1)


#Visualization parameters

#Age
sns.distplot(cars.Age)
sns.boxplot(y = cars.Age)

#Price
sns.distplot(cars['price'])
sns.boxplot(y = cars.price)

#powerPS
sns.distplot(cars.powerPS)
sns.boxplot(cars.powerPS)

#Age vs price
sns.regplot(x = 'powerPS',y = 'price',scatter = True,fit_reg = True,data = cars)
#car price higher are newer
#with increase in age price decreases

#powerPS VS price
sns.regplot(x = 'powerPS',y = 'price',scatter = True,fit_reg=False,data = cars)


#variable seller
cars.seller.value_counts()
pd.crosstab(cars.seller,columns = 'count',dropna=True,normalize=True)
sns.countplot(x = 'seller',data = cars,hue = 'price')
#we can remove this variable since it won't effect the price column

#variable offertype
cars.offerType.value_counts()
sns.countplot(x = 'offerType', data = cars)
#No effect on the price so we can remove it

#variable abtest
cars.abtest.value_counts()
pd.crosstab(cars.abtest,columns = 'count',normalize = True)
sns.countplot(x = 'abtest',data = cars)
#Equally distributed 
#For every price value there is 50-50 distribution
#Does not effect price

#Variable vehicleType
cars.vehicleType.value_counts()
pd.crosstab(cars.vehicleType,columns = 'Count',normalize = True)
sns.countplot(x = 'vehicleType',data = cars)
sns.boxplot(x = 'vehicleType',y = 'price',data = cars)
#Vehicle type affects price since limousine,small cars and station wagons has high 
#frequency

#Variable gearbox
cars.gearbox.value_counts()
pd.crosstab(cars.gearbox,columns = "count",normalize=True,dropna = True)
sns.countplot(x ="gearbox",data = cars )
sns.boxplot(x = "gearbox",y = 'price',data = cars)
#gearbox effects the price

# Variable model
cars.model.value_counts()
pd.crosstab(cars.model,columns = 'count',normalize=True)
sns.countplot(x = 'model',data = cars)
sns.boxplot(x = 'model',y = 'price',data = cars)
#many models are there
# It effects the price

# Variable kilometer
cars.kilometer.value_counts().sort_index()
pd.crosstab(cars.kilometer,columns = 'count',normalize = True)
sns.boxplot(x = "kilometer",y = "price",data = cars)
sns.distplot(cars.kilometer,bins = 8, kde = False)
sns.regplot(x = cars.kilometer,y = cars.price,scatter = True,fit_reg = True,data = cars)
# It effects price

# Variable fuelType
cars.fuelType.value_counts()
pd.crosstab( cars.fuelType,columns = "count",normalize = True)
sns.countplot(x = "fuelType",data = cars)
sns.boxplot(x = "fuelType",y = "price",data = cars)
# It effects price


#Variable brand
cars.brand.value_counts()
pd.crosstab(cars.brand,columns = "count",normalize = True)
sns.countplot(x = "brand",data = cars)
sns.boxplot(x = "brand",y = "price",data = cars)
# brand effects the price

# Variable notRepairedDamage
# yes - car is damaged but not rectified
# no - car is damaged but rectified
cars.notRepairedDamage.value_counts()
pd.crosstab(cars.notRepairedDamage,columns = "count",normalize = True)
sns.countplot(x = "notRepairedDamage",data = cars)
sns.boxplot(x = "notRepairedDamage",y = "price",data = cars)
# As expected cars with damages are fall under lower price ranges


# =============================================================================
# Removing Insignificant variables
# =============================================================================

col = ["seller","offerType","abtest"]
cars = cars.drop(col,axis = 1)
cars_copy = cars.copy()