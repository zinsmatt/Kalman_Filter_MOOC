from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

N=100
xbar = array([[1],[2]])
x=randn(2,N)
Γx = array([[3,1],[1,3]])
ax=init_figure(-10,10,-10,10)
ax.scatter(x[0],x[1])
draw_ellipse(xbar,Γx,0.9,ax,[1,0.8,0.8]) 

pause(1)