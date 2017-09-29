#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:55:43 2017

@author: wangshiru
"""

import numpy as np 

import matplotlib.pyplot as plt

V = [0.]  
t = [0.] 
g = 9.8 
dt = 0.1 
end_time = 100

for i in range(int(end_time / dt)):

	tmp = V[i] - g * dt

	V.append(tmp)

	t.append(dt * (i + 1))    

	print t[-1], V[-1]

plt.figure(figsize=(8,6)) 

plt.plot(t,V,label="V(t)",color="green",linewidth=5)

plt.xlabel("t(s)") 

plt.ylabel("V(m/s)") 

plt.legend()  

plt.show()  
