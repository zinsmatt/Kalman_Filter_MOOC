from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
mc,l,g,mr = 5,1,9.81,1
dt = 0.02

x = array([[0,2.5,0,0]]).T
Γα = (sqrt(dt)*(10**-3))**2*eye(4)


def f(x,u):
    s,θ,ds,dθ=x[0,0],x[1,0],x[2,0],x[3,0]
    dds=(mr*sin(θ)*(g*cos(θ)- l*dθ**2) + u)/(mc+mr*sin(θ)**2)
    ddθ= (sin(θ)*((mr+mc)*g - mr*l*dθ**2*cos(θ)) + cos(θ)*u)/ (l*(mc+mr*sin(θ)**2))
    return array([[ds],[dθ],[dds],[ddθ]])
    
ax=init_figure(-3,3,-3,3)

for t in arange(0,5,dt) :
    clear(ax)
    draw_invpend(ax,x)
    u = 0
    α=mvnrnd1(Γα)
    x = x + dt*f(x,u)+α  
pause(1)    
    