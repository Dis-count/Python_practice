from mpl_toolkits.axisartist.axislines import SubplotZero
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")

    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

plt.text(-2, 2, r"y=kx+b",
         horizontalalignment='center', fontsize=20)

x = np.linspace(-2,2,100)

k=-1
b=0

y = k*x + b

ax.plot(x, y)
plt.show()


#######################################
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
a1 = 2
a2 = 1
Z = a1*X+a2*Y

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.Blues,
                       linewidth=0, antialiased=False)

ax.set_xlabel(r'$x_1$',fontsize = 20, color = 'blue')
ax.set_ylabel(r'$x_2$',fontsize = 20, color = 'blue')
ax.set_zlabel(r'$x_3$',fontsize = 20, color = 'blue')
