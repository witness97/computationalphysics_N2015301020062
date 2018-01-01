#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:51:34 2018

@author: wangshiru
"""

import random
import turtle
wn=turtle.Screen()
wn.bgcolor('lightgreen')
tess=turtle.Turtle()
tess.color('hotpink')
tess.pensize(1)
for d in range (101):
    x=random.randrange(0,51)
    prob = random.random()
    tess.forward(x)
    tess.left(prob*360)
    tess.stamp()
wn.exitonclick()