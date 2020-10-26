import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



def f(x,y):
    return x*y

def gradient(x,y):
    return y, x

Q = np.array([[0.0, 0.5],
              [0.5, 0.0]])
L = np.array([0, 0])
c = 0.0

y, x = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-1, 1, 20))
dx, dy = gradient(x, y)

# gradients
plt.figure("Gradient de f")
plt.quiver(x, y, dx, dy)

# courbe de niveaux
z = f(x, y)
fig = plt.figure()
ax = fig.add_subplot(121, projection="3d", title="courbes de niveaux de f")
ax.contour(x, y, z, 10, cmap="jet")
ax2 = fig.add_subplot(122, projection="3d", title="f(x)")
ax2.plot_surface(x, y, z, cmap="jet")
plt.show()






def g(x, y):
    return 2*x**2 + x*y + 4 * y**2 + y - x + 3

Q = np.array([[2.0, 0.5],
              [0.5, 4.0]])
L = np.array([-1.0, 1.0])
c = 3.0

def gradient_g(X):
    return 2 * X @ Q + L

X = np.dstack((x, y))
deriv_g = gradient_g(X)

# gradients
plt.figure("Gradient de g")
plt.quiver(x, y, deriv_g[:, :, 0], deriv_g[:, :, 1])

# courbe de niveaux
z = g(x, y)
fig = plt.figure()
ax = fig.add_subplot(121, projection="3d", title="courbes de niveaux de g")
ax.contour(x, y, z, 10, cmap="jet")
ax2 = fig.add_subplot(122, projection="3d", title="g(x)")
ax2.plot_surface(x, y, z, cmap="jet")
plt.show()

minimum = -L @ np.linalg.inv(Q) * 0.5
print("Minimum de g en ", minimum)

