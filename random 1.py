#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 11:53:31 2018

@author: wangshiru
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

steps = np.linspace(0, 100, 101)
x_ave = np.zeros(101)
x_y0 = np.zeros(101)
x_now = np.zeros(4000)

for i in range(100):
    for j in range(4000):
        ruler = np.random.rand()
        if ruler<=0.5:
            x_now[j] = x_now[j] + 1
        else:
            x_now[j] = x_now[j] - 1
    average = sum(x_now)/4000
    x_ave[i+1] = average
    
plt.scatter(steps, x_ave)
plt.plot(steps, x_y0)
plt.xlim(0,100)
plt.ylim(-1,1)
plt.grid(True)
plt.xlabel('step number(= time)')
plt.ylabel('<x>')
plt.title('<x> of 4000 walkers')

plt.show()