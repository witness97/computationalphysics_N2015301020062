#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 22:34:44 2017

@author: wangshiru
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation

delta_x=0.01
c=300
delta_t=delta_x/c
r=1

x=np.linspace(0,1,int(1/delta_x)+1)

def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next

def after_n_step(y0,y1,n):#n=T/delta_t
    for i in range(n):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
    return y0,y1

# initialize y- one Gaussian wavepacket,k0,x0
k0,x0=300,0.6
k1,x1=300,0.6
y_initial=[]
for i in range(1+int(1/delta_x)):
    #y_initial.append(math.exp(-k0*(i*delta_x-x0)**2))
    #y_initial.append(-2*math.exp(-k1*(i*delta_x-x1)**2))
    y_initial.append(math.exp(-k0*(i*delta_x-x0)**2)-2*math.exp(-k1*(i*delta_x-x1)**2))



#plot.n_step is time interval, n_plot is the nomber of subplot
n_step=11
n_plot=11
y0,y1=y_initial,y_initial
plt.subplot(n_plot,1,1)
plt.plot(x,y1)
plt.title('Waves On A String With Fixed Ends,Two Wavepackets')#k,x=300,0.6 #k,x=1000,0.3
plt.xticks([])
plt.yticks([])
plt.ylim(-2.01,2.01)#plt.ylim(-1.01,1.01)
plt.text(0.85,0.,'step n=0')

for i in range(n_plot-1):
    y0,y1=after_n_step(y0,y1,n_step)
    plt.subplot(n_plot,1,i+2)
    plt.text(0.85,0.,'step n=%s'%(n_step*(i+1)))
    plt.yticks([])
    plt.ylim(-2.01,2.01)#plt.ylim(-1.01,1.01)
    if i<n_plot-2:
        plt.xticks([])
    plt.plot(x,y1)

plt.show()


# first set up the figure, the axis, and the plot element we want to animate   
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-2.01,2.01))
line, = ax.plot([], [], lw=1.)  
plt.title('Waves On A String With Fixed Ends')
plt.xlabel('x')
plt.ylabel('displacement')
note = ax.text(0.05,1.4,'',fontsize=12)#note = ax.text(0.65,0.8,'',fontsize=12)
# initialization function: plot the background of each frame
def init():  
    line.set_data([], []) 
    note.set_text('')
    return line,note
# animation function.  this is called sequentially   
def animate(j):
    y0,y1=after_n_step(y_initial,y_initial,j)
    line.set_data(x, y1)
    note.set_text(r'$y_0=exp[-%s\times (x-%s)^2]-2*exp[-%s\times (x-%s)^2]$'%(k0,x0,k1,x1)+'\nstep n=%s'%j)#change the initial displacement accordingly
    return line,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=201, interval=50)#, blit=True) 
#anim1.save('/home/shangguan/ex14/gif3/haha.png')
plt.show()  