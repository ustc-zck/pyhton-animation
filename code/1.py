import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

max_distance = 1.521e11
min_distance = 1.471e11

a = (max_distance + min_distance) / 2
c = (max_distance - min_distance) / 2
b = (a**2 - c**2)**0.5

#r = b**2 / (a + c*np.cos(theta))

theta = np.pi / 12

xdata = [a * np.cos(i / np.pi) for i in range(0, 360)]
ydata = [b * np.sin(i / np.pi) for i in range(0, 360)]

fig, ax = plt.subplots()

t = [i/np.pi for i in np.arange(0,360)]

x = a * np.cos(t)
y = b * np.sin(t)

plt.scatter([c,],[0,], 200, color = 'red')

l = ax.plot(x, y, color = 'blue')
dot, = ax.plot([], [], 'ro')
line, = ax.plot([], [], 'o-', lw = 2)
line_1, = ax.plot([], [], 'o-', lw = 2)
def init():
    ax.set_xlim(-a, a)
    ax.set_ylim(-b, b)
    return l, line, line_1

def update(i):
    newx = [c, xdata[i]]
    newy = [0, ydata[i]]
    line.set_data(newx, newy)
    newx_1 = [c, xdata[i + 1]]
    newy_1 = [0, ydata[i + 1]]
    line_1.set_data(newx_1, newy_1)
    return line,line_1

ani = animation.FuncAnimation(fig, update, range(0, 360), interval = 50, init_func=init)

plt.show()

