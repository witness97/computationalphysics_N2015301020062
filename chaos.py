import matplotlib.pyplot as plt
import numpy as np
import math
a0 = 0.2
a1 = 0.201
FD = float(input('FD='))


gl = 1.0
Ωd = 0.67
q = 0.5
dt = 0.04
m = math.pi


list1 = [0]
list2 = [a0]
list3 = [a1]
n = math.log(a1-a0)
list4 = [n]
list5 = [0]
list6 = [0]
i = 0
while i < 5000:
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
    wx2 = list6[i]
    ax = list3[i]
    w2 = wx2 - gl * dt * np.sin(ax) - q * wx2 * dt + FD * dt * np.sin(Fx)
    list6.append(w2)
    a = ax + wx2 * dt
    while a > m:
        a -= m*2
    while -a > m:
        a += m*2
    list3.append(a)
    t += dt
    list1.append(t)
    i += 1
    da0 = list3[i] - list2[i]
    da1 = abs(da0)
    da2 = math.log(da1)
    list4.append(da2)
T = np.array(list1)
A1 = np.array(list2)
A2 = np.array(list3)
DA = np.array(list4)
W1 = np.array(list5)
W2 = np.array(list6)
plt.figure(figsize=(8,6))

plt.plot(T,A1,color="red", linewidth=1.2, linestyle="-",label="a(0)=0.2")
plt.plot(T,A2,color="blue", linewidth=1.2, linestyle="-",label="a(0)=0.201")
plt.ylabel("angle (radians)")
plt.title("angle versus time")
plt.xlabel("t (s)")
plt.legend()
plt.show()
    

plt.plot(T,DA,color="red", linewidth=1.2, linestyle="-",label="da(0)=0.01")
plt.ylabel("d_angle (radians)")
plt.title("d_angle versus time")
plt.xlabel("t (s)")
plt.legend()
plt.show()


plt.plot(A1,W1,color="red", linewidth=1.2, linestyle="-",label="a(0)=0.2")

plt.ylabel("Angular velocity (rad/s)")
plt.title("Angular velocity versus angle")
plt.xlabel("θ (rad)")
plt.legend()
plt.show()


plt.plot(A2,W2,color="blue", linewidth=1.2, linestyle="-",label="a(0)=0.201")

plt.ylabel("Angular velocity (rad/s)")
plt.title("Angular velocity versus angle")
plt.xlabel("θ (rad)")
plt.legend()
plt.show()