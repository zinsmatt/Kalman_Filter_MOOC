from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py


def draw_ellipse(c, Γ, η, col, width=1):
    if (norm(Γ)==0):
        Γ=Γ+0.001*eye(len(Γ[1,:]))
    A=sqrtm(-2*log(1-η)*Γ)
    w,v=eig(A)
    v1=array([[v[0,0]],[v[1,0]]])
    v2=array([[v[0,1]],[v[1,1]]])

    f1=A @ v1
    f2=A @ v2
    angle =  (arctan2(v1 [1,0],v1[0,0]))

    I = arange(0, 2*pi+0.1, 0.1)
    x = norm(f1) * cos(I)
    y = norm(f2) * sin(I)
    pts = np.vstack((x, y))
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle), np.cos(angle)]])
    pts = R @ pts
    pts += np.asarray(c).reshape((2, 1))
    plot2D(pts, col, width)




def simu(x,u):
    return (array([x[3]*cos(x[4])*cos(x[2]),
                       x[3]*cos(x[4])*sin(x[2]),
                       x[3]*sin(x[4])/3,
                       u[0],
                       u[1]]))


dt = 0.15
u = array([[0, 0]]).T
x = array([[0, 0, pi/3, 4, 0.3]]).T

Galpha = array([[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0.01*dt,0,0],
                [0,0,0,0.01*dt,0],
                [0,0,0,0,0.01*dt]])

ax=init_figure(-50,50,-50,50)

# on mesure x[4] et x[2]
zhat = array([x[0],  x[1], x[3]])
Gz = np.zeros((3, 3))
Galphaz = dt * np.diag([0.01, 0.01, 0.01])


for t in arange(0, 20, dt) :
    clear(ax)
    
    # simu
    x = x + dt * simu(x,u) + mvnrnd1(Galpha)

    uz = array([[0, 0, dt*u[0, 0]]]).T
   
    Ak = np.array([[1.0, 0.0, dt*np.cos(x[4,0])*np.cos(x[2,0])],
                   [0.0, 1.0, dt*np.cos(x[4,0])*np.sin(x[2,0])],
                   [0.0, 0.0, 1.0]])

    # Sans mesurer la vitesse
    # y = np.zeros((0, 1))
    # C = np.zeros((0, 3))
    # Gbeta = np.zeros((0, 1))
    
    # Avec mesure de la vitesse
    y = np.array([x[3]]) + mvnrnd1(0.1)
    C = np.array([[0.0, 0.0, 1.0]])
    Gbeta = np.array([[0.1]])

    zhat, Gz = kalman(zhat, Gz, uz, y, Galphaz, Gbeta, Ak, C)
    draw_ellipse(zhat[:2, 0], Gz[:2, :2], 0.99, 'black')

    draw_car(x)  	
