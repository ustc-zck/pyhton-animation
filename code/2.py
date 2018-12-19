import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

#Jupiter,Saturn,Uranus,Neptune
list_a = [7.785472e11,1.43344937e12, 2.876679082e12, 4.503443661e12]
list_e = [0.048775, 0.055723219,0.044405586, 0.011214269]


list_b = []

for i in range(len(list_a)):
    a = list_a[i]
    e = list_e[i]
    c = a * e
    b = (a**2 - c**2)**0.5
    list_b.append(b)

t = [i/np.pi for i in np.arange(0,360)]

fig, ax = plt.subplots()

plt.scatter([c,], [0], color = 'yellow')

dot0, = ax.plot([], [], 'ro')
dot1, = ax.plot([], [], 'ro')
dot2, = ax.plot([], [], 'ro')
dot3, = ax.plot([], [], 'ro')

a0 = list_a[0]
b0 = list_b[0]

x0 = a0 * np.cos(t)
y0 = b0 * np.sin(t)
l0 = ax.plot(x0, y0)


a1 = list_a[1]
b1 = list_b[1]

x1 = a1 * np.cos(t)
y1 = b1 * np.sin(t)
l1 = ax.plot(x1, y1)

a2 = list_a[2]
b2 = list_b[2]

x2 = a2 * np.cos(t)
y2 = b2 * np.sin(t)
l2 = ax.plot(x2, y2)


a3 = list_a[3]
b3 = list_b[3]

x3 = a3* np.cos(t)
y3 = b3 * np.sin(t)
l3 = ax.plot(x3, y3)

def init():
    ax.set_xlim(-a3, a3)
    ax.set_ylim(-b3, b3)
    return l0, l1, l2, l3

point0 = []
point1 = []
point2 = []
point3 = []

for i in np.arange(0,3600):
    point0.append([a0*np.cos(i/(10 * np.pi)), b0 * np.sin(i / (np.pi * 10))])
    point1.append([a1*np.cos(i/(10 * np.pi)), b1 * np.sin(i / (np.pi * 10))])
    point2.append([a2*np.cos(i/(10 * np.pi)), b2 * np.sin(i / (np.pi * 10))])
    point3.append([a3*np.cos(i/(10 * np.pi)), b3 * np.sin(i / (np.pi * 10))])

def update_dot(i):
    dot0.set_data(point0[i][0], point0[i][1])
    dot1.set_data(point1[i][0], point1[i][1])
    dot2.set_data(point2[i][0], point2[i][1])
    dot3.set_data(point3[i][0], point3[i][1])
    return dot0, dot1, dot2, dot3

ani = animation.FuncAnimation(fig, update_dot, range(0,3600), interval = 100, init_func=init)

plt.legend()
plt.show()
