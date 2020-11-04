from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py


x, y = meshgrid(arange(-7,7,0.1), arange(-7,7,0.1))


# 1)
X_bar = np.array([1.0, 2.0])

cov = np.array([[1.0, 0.0],
                [0.0, 1.0]])

cov_inv = np.linalg.inv(cov)


Q = cov_inv[0, 0] * (x - X_bar[0])**2 \
    + 2 * cov_inv[0, 1] * (x - X_bar[0]) * (y - X_bar[1]) \
    + cov_inv[1, 1] * (y - X_bar[1])**2

z = 1.0 / (np.sqrt((2 * np.pi))**2 * np.linalg.det(cov)) * np.exp(-0.5 * Q)



fig = figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z)
fig = figure()
contour(x, y, z)


# 2)
# La nouvelle Gaussienne a bien été étirée suivant y, puis tournée de pi/6.
# Son centre a été translaté de [2, -5]

alpha = np.pi / 6
A = np.array([[np.cos(alpha), -np.sin(alpha)],
              [np.sin(alpha), np.cos(alpha)]])
S = np.array([[1.0, 0.0],
              [0.0, 2.0]])
A = A @ S
b = np.array([2, -5])

Y_bar = A @ X_bar + b
cov_Y = A @ cov @ A.T
cov_Y_inv = np.linalg.inv(cov_Y)

Q_Y = cov_Y_inv[0, 0] * (x - Y_bar[0])**2 \
      + 2 * cov_Y_inv[0, 1] * (x - Y_bar[0]) * (y - Y_bar[1]) \
      + cov_Y_inv[1, 1] * (y - Y_bar[1])**2

z_Y = 1.0 / (np.sqrt((2 * np.pi))**2 * np.linalg.det(cov_Y)) * np.exp(-0.5 * Q_Y)


fig = figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z_Y)
fig = figure()
contour(x, y, z_Y)
