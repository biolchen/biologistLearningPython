## show 1 figure with multiple subfigures
import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, linspace, pi, sin, tan
plt.close()
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
fig = plt.figure(1)  # an empty figure with no axes
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'ko-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')

plt.subplot(1, 2, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')

plt.show()
## Show multiple figures

x1 = x2 = linspace(0, 4 * pi, 100)
y1 = sin(x1)
y2 = cos(x2)
y3 = tan(x1)
plt.figure(1)
plt.plot(x1, y1, "b-*")
plt.figure(2)
plt.plot(x2, y2, "r-h")
plt.figure(3)
plt.plot(x1, y3, "k-p")
plt.show()

## Empty figures
fig = plt.figure(4)  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
fig.show()
##
