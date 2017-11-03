import matplotlib.pyplot as plt
import numpy as np
import math
a0 = 0.2

FD = float(input('FD='))



gl = 1.0

q = 0.5
dt = 0.04
m = math.pi
Ωd = 0.2*m


list1 = [0]
list2 = [a0]

list5 = [0]
list6 = [0]
list7 = [0]
list8 = [0]
i = 0
j = 0
while i < 1000000:
    t = list1[i]
    wx1 = list5[i]
    ax = list2[i]
    Fx = Ωd * t
    w1 = wx1 - gl * dt * np.sin(ax) - q * wx1 * dt + FD * dt * np.sin(Fx)
    list5.append(w1)
    a = ax + wx1 * dt
    while a > m:
        a -= m*2
    while -a > m:
        a += m*2
    list2.append(a)


    t += dt
    list1.append(t)
    i += 1

    
while j < 1000000:  
    list8.append(list5[j])
    list7.append(list2[j])
    j += 250
    
    
    

Q1 = np.array(list7)
Q2 = np.array(list8)
plt.figure(figsize=(8,6))





plt.scatter(Q1,Q2,color="red",marker=".")


plt.show()