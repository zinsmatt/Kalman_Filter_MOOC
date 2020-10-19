from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
N=10
X=randn(2,N)
print('X=',X)

xbar = array([[1],[2]])
Γx = array([[3,1],[1,3]])


ax=init_figure(-10,10,-10,10)
draw_ellipse(xbar,Γx,0.999,ax,[1,0.8,0.8])    
pause(1)