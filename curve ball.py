#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:15:47 2017

@author: wangshiru
"""

import matplotlib.pyplot as plt
import numpy as np
import math

v = float(input('v='))
v0 = v
a = float(input('a='))
g = 9.8
a1 = 0.079
a2 = 0.06
s=0.00041
b=0.0039+0.0058/(1+math.exp((v-35)/5))
w=float(input('w='))*3.14/60
v= float(v)
a1= float(a1)
a2 = float(a2)
dt = 0.001


plt.figure(figsize=(8,5))
plt.xlim(0,9)
plt.ylim(-0.05,0.05)
plt.xlabel("x (m)")
plt.ylabel("y (m)/z (m)")

plt.title("curve ball")


i=0
list1 = [0]
list2 = [0]
list3 = [0]
list4 = [0]
list5 = [0]
ra1 = a1 * 3.14 / 180
ra2 = a2 * 3.14 / 180
ra3 = a * 3.14 / 180
vx = v * np.cos(ra1)* np.cos(ra2)
vy = v * np.sin(ra1)* np.cos(ra2)
vz = v * np.cos(ra1)*np.sin(ra2)
vx1 = v0 * np.cos(ra3)
vy1 = v0 * np.cos(ra3) 
while list2[i] >= 0:
    x = list1[i] + vx * dt
    list1.append(x)
    y = list2[i] + vy * dt
    list2.append(y)
    z = list3[i] + vz * dt
    list3.append(z)        
    vy -= g * dt
    vx -= b * v * vx * dt
    vz -= s * vx * w * dt
    v = math.sqrt(vx*vx+vy*vy+vz*vz)
    i += 1
i=0
while list5[i] >= 0 :
    x = list4[i] + vx1 * dt
    list4.append(x)
    y = list5[i] + vy1 * dt
    list5.append(y) 
    vy1  -= g * dt
    i += 1
    
X=np.array(list1)
Y=np.array(list2)
Z=np.array(list3)
X1=np.array(list4)
Y1=np.array(list5) 
plt.plot(X,Y,color="red", linewidth=2.5, linestyle="-",label="Y")
plt.plot(X,Z,color="blue", linewidth=2.5, linestyle="-",label="Z") 
plt.plot(X1,Y1,color="green", linewidth=5, linestyle="-",label="orign")
plt.legend(loc='upper left')  
