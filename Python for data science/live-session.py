# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y1 = np.array([5,9,3,7,2])
y2 = np.array([3,6,8,2,4])

plt.plot(x,y1 , label = 'Array 1' ,marker = 'o' ,linestyle = ':',color = 'b')
plt.plot(x,y2,label = 'Array 2', marker = 'x' , linestyle = '-.',color = 'c')

plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title("Two Arrays in the same plot")

plt.legend()

plt.grid(True)

plt.show()

         # plt.plot?