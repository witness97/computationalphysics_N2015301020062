#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:38:00 2018

@author: wangshiru
"""

from pylab import *
from random import choice
numwalk = 6
length = 200
data = zeros((numwalk, length), int)
for n in range(numwalk):
	for x in range(1, length):
		step = choice([-1, 1])
		data[n,x] = data[n,x-1] + step
	plot(range(length), data[n,:])
xlabel('t')
axis ((0,200, -20, 20))
savefig('Random_Walk_example.svg')
show()
