from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_pend(θ,col='black'): #inverted pendulum
    plot( [0,sin(θ)],[0,-cos(θ)],col, linewidth = 2)
    
def f(x,u):
    θ,dθ=x[0,0],x[1,0]
    return array([[dθ],[-sin(θ)+u]])    

ax=init_figure(-2,2,-2,2)
dt = 0.01
sigm_x=0.05    
x = array([[1,0]]).T
Γα = dt * sigm_x**2 * eye(2)
u=0
for t in arange(0,0.1*1,dt) :
    clear(ax)
    draw_pend(x[0,0],"black")
    x=x+dt*f(x,u)+mvnrnd1(Γα)
    pause(0.001)

