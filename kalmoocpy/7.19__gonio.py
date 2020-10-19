from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

La = array([[0,15,30,15],
              [25,30,15,20]])

def f(x,u):
    x=x.flatten()
    u=u.flatten()
    return (array([[x[3]*cos(x[4])*cos(x[2])],
                    [x[3]*cos(x[4])*sin(x[2])],
                    [x[3]*sin(x[4])/3],
                    [u[0]],
                    [u[1]]]))


    
def g(x):
    x=x.flatten()
    for i in range(La.shape[1]):
        C = array([[0,0,1]])
        y=array([[x[3]]])
        Beta = [1]
        a=La[:,i].flatten()
        da = a-(x[0:2]).flatten()
        dist = norm(da)      
        if dist < 15:
            plot(array([a[0],x[0]]),array([a[1],x[1]]),"red",1)
            δ=arctan2(da[1],da[0])
            Ci = array([[-sin(δ),cos(δ), 0]])
            C = vstack((C,Ci))          
            yi=[[-sin(δ)*a[0] + cos(δ)*a[1]]]
            y = vstack((y,yi)) 
            Beta.append(1)
    Γβ = diag(Beta)
    y = y + mvnrnd1(Γβ)
    return(C,y,Γβ)    
            
        
dt = 0.1
ua = array([[0]] * 2)
xa = array([[-20,-25,pi/3,15,0.1]]).T
Γαxa = diag([dt*0.001,dt*0.001,0,dt*0.001,0])
ax=init_figure(-100,100,-100,100)

for t in arange(0,10,dt) :   
    clear(ax)
    draw_car(xa)
    scatter(La[0], La[1])
    θa,δa = xa[2],xa[4]
    draw_car(xa)
    Ca,ya,Γβa = g(xa)
    xa = xa + dt*f(xa,ua) + mvnrnd1(Γαxa)        
pause(1)    
    
    
    
       
