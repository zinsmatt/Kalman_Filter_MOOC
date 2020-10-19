
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
xhat = array([[0,1]]).T
Γx = array([[0.7,0.3],[0.3,0.2]])
ax=init_figure(-1,12,-1,2)
clear(ax)
draw_ellipse(xhat, Γx, 0.99,ax,'red')
pause(1)   