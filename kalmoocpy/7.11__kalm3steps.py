from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
ax=init_figure(-30,30,-30,30)
C = array([[1,1]])
y = 3
Γβ = 1
x0 = array([[0],[0]])
Γ0 = array([[100,0],[0,100]]) 
draw_ellipse(x0,Γ0,0.9,ax,[0.8,0.8,1])
pause(1.0)
xup,Γup = kalman_correc(x0,Γ0,y,Γβ,C)
draw_ellipse(xup,Γup,0.9,ax,[1,0.8,0.8])
pause(1.0)
