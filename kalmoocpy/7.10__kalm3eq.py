from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
x = array([[0,0]]).T
Γ = 50*eye(2)
ax=init_figure(-100,100,-100,100)
draw_ellipse(x,Γ,0.99,ax,[1,0.8,0.8])
pause(1)




