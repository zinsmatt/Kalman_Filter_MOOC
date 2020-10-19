from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def f(x,u):
    x,u=x.flatten(),u.flatten()
    θ,v=x[2],x[3]
    xdot=array([[v*cos(θ)],[v*sin(θ)],[u[0]],[u[1]]])
    return xdot


x = array([[0],[0],[0],[1]])
u = array([[0.1],[0]])
dt= 0.1
ax=init_figure(-20,20,-20,20)
for t in np.arange(0, 5, dt):
    clear(ax)
    m=array([[6+2*sin(t),7+3*cos(t)]]).T
    Γα = diag([1,1,1,1])         
    x=x+dt*f(x,u)
    draw_tank(x)
    ax.plot(m[0],m[1], '*r')	
pause(1)



