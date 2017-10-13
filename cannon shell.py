#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:08:01 2017

@author: wangshiru
"""

import matplotlib.pyplot as plt
import numpy as np
list1 = [0,0]
list2 = [0,0]
v = input('v=')
g = 9.8
a = input("a=")
v= float(v)
a= float(a)
ra = a * 3.14 / 180
vx = v * np.cos(ra)
vy = v * np.sin(ra)
dt = 1
list1[1] = list1[0] + vx * dt
list2[1] = list2[0] + vy * dt
vy -= g * dt
i = 1
while list2[i] >= 0:
    x = list1[i] + vx * dt
    list1.append(x)
    y = list2[i] + vy * dt
    list2.append(y)
    vy -= g * dt
    i += 1
X1 = np.array(list1)
Y1 = np.array(list2)
plt.figure(figsize=(8,6))
plt.plot(X1,Y1,color="red", linewidth=2.5, linestyle="-")
plt.xlabel("y (m)")
plt.ylabel("x (m)")
plt.title("Cannon shell")
plt.xlim(0,60000)
plt.ylim(0,20000)
plt.legend()
plt.show()