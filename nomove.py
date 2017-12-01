#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:03:39 2017

@author: wangshiru
"""

import math
import matplotlib.pyplot as plt
from matplotlib import animation


G=4*math.pi**2
MS=1
ME=3*10**(-6)
MJ=1.9*10**(-3)/2
Gs=G*MS

def NoStaSun(me,mj,dt,T):
    Gj=G*mj
    Ge=G*me
    re=[[]for i in range(2)]
    rj=[[]for i in range(2)]
    rs=[[]for i in range(2)]
    ve=[[]for i in range(2)]
    vj=[[]for i in range(2)]
    vs=[[]for i in range(2)]
   
    re[0].append(1.00)
    re[1].append(0.00)
    rj[0].append(5.20)
    rj[1].append(0.00)
    rs[0].append(0.00)
    rs[1].append(0.00)
    ve[0].append(0.00)
    ve[1].append(2*math.pi)
    vj[0].append(0.00)
    vj[1].append(2*math.pi/math.sqrt(5.2))
    vs[0].append(0.00)
    vs[1].append(0.00)
    for i in range(int(T/dt)):
        de=math.sqrt((re[0][-1]-rs[0][-1])**2+(re[1][-1]-rs[1][-1])**2)
        dj=math.sqrt((rj[0][-1]-rs[0][-1])**2+(rj[1][-1]-rs[1][-1])**2)
        dej=math.sqrt((re[0][-1]-rj[0][-1])**2+(re[1][-1]-rj[1][-1])**2)
        for k in range(2):
            ve[k].append(ve[k][-1]+(Gs*(rs[k][-1]-re[k][-1])/de**3+Gj*(rj[k][-1]-re[k][-1])/dej**3)*dt)
            vj[k].append(vj[k][-1]+(Gs*(rs[k][-1]-rj[k][-1])/dj**3+Ge*(re[k][-1]-rj[k][-1])/dej**3)*dt)
            vs[k].append(vs[k][-1]+(Ge*(re[k][-1]-rs[k][-1])/de**3+Gj*(rj[k][-1]-rs[k][-1])/dj**3)*dt)
            re[k].append(re[k][-1]+ve[k][-1]*dt)
            rj[k].append(rj[k][-1]+vj[k][-1]*dt)
            rs[k].append(rs[k][-1]+vs[k][-1]*dt)
    return rs,re,rj


def NoStaSunCOM(me,mj,dt,T,rs,re,rj):
    rcom_x=me*1+mj*5.2
    vcom_y=me*2*math.pi+mj*2*math.pi/math.sqrt(5.2)
    ycom=[]
    rsc,rec,rjc=[[]for i in range(2)],[[]for i in range(2)],[[]for i in range(2)]
    for i in range(int(T/dt)+1):
        ycom.append(vcom_y*i*dt)
    rsc[0]=map(lambda x:x-rcom_x,rs[0])
    rjc[0]=map(lambda x:x-rcom_x,rj[0])
    rec[0]=map(lambda x:x-rcom_x,re[0])
    rsc[1]=map(lambda x,y:x-y, rs[1],ycom)
    rec[1]=map(lambda x,y:x-y, re[1],ycom)
    rjc[1]=map(lambda x,y:x-y, rj[1],ycom)
    return rsc,rec,rjc



n=float(input('the mass of Jupiter divided by its real mass is='))
me,mj = ME,MJ*n
rs,re,rj=NoStaSun(me,mj,0.001,15)
rsc,rec,rjc=NoStaSunCOM(me,mj,0.001,15,rs,re,rj)
plt.subplot(1,2,1)
plt.plot(rj[0],rj[1],label='Jupiter')
plt.plot(re[0],re[1],label='Earth')
plt.plot(rs[0],rs[1],label='Sun')
plt.title('Three-body Simulation,Rest Frame')
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.text(-5.9,3.6,r'The Sun Is NOT Stationary'+'\nMass of Jupiter=%s$m_J$'%(mj/MJ)+'\nMass of Earth=%s$m_E$'%(me/ME)+'\nMass of Sun=$m_S$')
plt.legend()

plt.show()



def init():  
    linej.set_data([], []) 
    linee.set_data([],[])
    lines.set_data([],[])
    note.set_text('') 
    return linej,linee,lines,note
 
def animate(j):
    me=ME
    mj=MJ*j*5
    rs,re,rj=NoStaSun(me,mj,0.001,15)
  
    linej.set_data(rj[0],rj[1])
    linee.set_data(re[0],re[1]) 
    lines.set_data(rs[0],rs[1])
    note.set_text(r'The Sun Is NOT Stationary'+'\nMass of Jupiter=%d$M_J$'%(mj/MJ))
    
    return linej,linee,lines,note
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=120, interval=30)

plt.show()