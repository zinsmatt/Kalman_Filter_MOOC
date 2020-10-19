from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
C_liste = [array([[4,0]]),array([[10,1]]),array([[10,5]]),array([[13,5]]),array([[15,3]])]
y_liste = [5,10,11,14,17]
xhat = array([[1],[-1]])
Γx = 4*eye(2)
ax=init_figure(-7,7,-7,7)
draw_ellipse(xhat,Γx,0.9,ax,[0.8,0.8,0.8])
pause(1)