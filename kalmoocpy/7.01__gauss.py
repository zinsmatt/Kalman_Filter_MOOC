from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
x, y = meshgrid(arange(-5,5,0.1), arange(-5,5,0.1))
z=exp(-((x-1)**2 + y**2+(x-1)*y))
fig = figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z)
fig = figure()
contour(x,y,z)

