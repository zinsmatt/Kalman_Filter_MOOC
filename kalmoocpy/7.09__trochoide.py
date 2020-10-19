from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
y = array([[0.38,3.25,4.97,-0.26]]).T
ax=init_figure(-5,40,-3,8)
p=array([3,2])
t = arange(0,20,0.1)
ax.plot(p[0]*t - p[1]*sin(t) , p[0] - p[1]*cos(t),'green')
pause(1)



