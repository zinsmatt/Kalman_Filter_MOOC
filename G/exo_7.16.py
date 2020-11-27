from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_invpend(ax,x, w): #inverted pendulum
    s,θ=x[0,0],x[1,0]
    draw_box(ax,s-0.7,s+0.7,-0.25,0,'blue')
    plot( [s,s-sin(θ)],[0,cos(θ)],'magenta', linewidth = 2)
    plt.plot(w, 0, "or")

mc,l,g,mr = 5,1,9.81,1
dt = 0.04

x = array([[0,0.4,0,0]]).T
Γα = (sqrt(dt)*(10**-3))**2*eye(4)


def f(x,u):
    s,θ,ds,dθ=x[0,0],x[1,0],x[2,0],x[3,0]
    dds=(mr*sin(θ)*(g*cos(θ)- l*dθ**2) + u)/(mc+mr*sin(θ)**2)
    ddθ= (sin(θ)*((mr+mc)*g - mr*l*dθ**2*cos(θ)) + cos(θ)*u)/ (l*(mc+mr*sin(θ)**2))
    return array([[ds],[dθ],[dds],[ddθ]])
    
ax=init_figure(-3,3,-3,3)

A = np.array([[0.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 1.0],
              [0.0, mr*g/mc, 0.0, 0.0],
              [0.0, (mc+mr) * g / (l*mc), 0.0, 0.0]])

B = np.array([[0.0, 0.0, 1/mc, 1/(l*mc)]]).T

K = place_poles(A, B, [-2.0, -2.1, -2.2, -2.3]).gain_matrix

E = array([[1, 0, 0, 0]])
h = -inv(E @ inv(A - B @ K) @ B)

C = np.array([[1.0, 0.0, 0.0, 0.0],
              [0.0, 1.0, 0.0, 0.0]])

# L = place_poles(A.T, C.T, [-2.0, -2.1, -2.2, -2.3]).gain_matrix.T

xhat = np.zeros((4, 1))
Gx = eye(4)
Galpha = eye(4) * dt * 0.0001
Gbeta = 0.0001 * eye(2)

w = 2
for ti, t in enumerate(arange(0,10,dt)):
    clear(ax)
    draw_invpend(ax,x, w)

    u = (-K @ xhat + h * w).item()
    y = C @ x + 0.01 * randn(2, 1)
    
    # Estimateur de Luenberger
    # xhat = xhat + (A @ xhat + B * u - L @ (C @ xhat - y)) * dt
    
    # Estimateur avec Kalman
    xhat, Gx = kalman(xhat, Gx, dt * B * u, y, Galpha, Gbeta, eye(4 ) + dt * A, C)
        
    α=mvnrnd1(Γα)
    x = x + dt*f(x,u)+α  
    
    plt.savefig("out/img_%04d.png" % ti)
    