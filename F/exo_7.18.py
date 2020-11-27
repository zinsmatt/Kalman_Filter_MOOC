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


    
def g(x):
    x=x.flatten()
    Beta = [1]
    y=[x[3]]
    C = [[0.0, 0.0, 1.0]]
    for i in range(La.shape[1]):
        a=La[:,i].flatten()
        da = a-(x[0:2]).flatten()
        if norm(da) < 15:
            plot(array([a[0],x[0]]),array([a[1],x[1]]),"red",1)
            delta=arctan2(da[1],da[0]) - x[2]
            Ci = array([[-sin(delta+x[2]),cos(delta+x[2]), 0]])
            C.append(Ci)
            yi=-sin(delta+x[2])*a[0] + cos(delta+x[2])*a[1]
            y.append(yi)
            Beta.append(1)
    Gbeta = diag(Beta)
    y = np.vstack(y).reshape((-1, 1))
    C = np.vstack(C)
    y = y + mvnrnd1(Gbeta)
    return(C,y,Gbeta)    
            

    
def gab(xa, xb):
    
    # Robot a voit robot b
    dab = xb[:2, 0] - xa[:2, 0]
    phi = arctan2(dab[1], dab[0]) - xa[2, 0]

    if norm(dab) < 15:
        plot([xa[0, 0], xb[0, 0]], [xa[1, 0], xb[1, 0]], 'red', 1)
        Cab = np.array([-sin(xa[2, 0]+phi), cos(xa[2, 0]+phi), 0, sin(xa[2, 0]+phi), -cos(xa[2, 0]+phi), 0.0])
        Gab = np.ones((1, 1))
        yab = np.zeros((1, 1)) + mvnrnd1(Gab)
        return Cab, yab, Gab
    else:
        return None, None, None
    
    

def gall(xa, xb):
    Ca, ya, Ga = g(xa)
    Cb, yb, Gb = g(xb)
    Cab_, yab_, Gab_ = gab(xa, xb)
    Cab = block_diag(Ca, Cb)
    yab = np.vstack((ya, yb))

    Gab = block_diag(Ga, Gb)

    
    if Cab_ is not None:
        Cab = np.vstack((Cab, Cab_)) 
        yab = np.vstack((yab, yab_)) 
        Gab = block_diag(Gab, Gab_)

    return Cab, yab, Gab
        
            
        
dt = 0.05

ax=init_figure(-50,50,-50,50)


def one_car():
    ua = array([[0]] * 2)
    xa = array([[-10,-25,pi/4,20,0.1]]).T
    Galphaxa = diag([dt*0.001,dt*0.001,0,dt*0.001,0])

    zhat = np.array([[0.0, 0.0, 0.0]]).T
    Gz = 1e3 * eye(3)
    Gzalpha = dt * 0.01 * eye(3)

    
    for t in arange(0,10,dt) :   
        clear(ax)
        draw_car(xa)
        scatter(La[0], La[1])
        
        Ck, yk, Gbetak = g(xa)
        
        Ak = np.array([[1.0, 0.0, dt*np.cos(xa[4,0])*np.cos(xa[2,0])],
                       [0.0, 1.0, dt*np.cos(xa[4,0])*np.sin(xa[2,0])],
                       [0.0, 0.0, 1.0]])
        uk = np.array([[0.0, 0.0, dt*ua[0,0]]]).T
        
        zhat, Gz = kalman(zhat, Gz, uk, yk, Gzalpha, Gbetak, Ak, Ck)
        draw_ellipse(zhat[:2,0], Gz[:2, :2], 0.9, "green", 2)
        
        alpha = xa * 0
        alpha[[0, 1, 3], 0] += mvnrnd1(Gzalpha).flatten()
        xa = xa + dt*f(xa,ua) + alpha




def two_cars():
    ua = array([[0]] * 2)
    ub = array([[0]] * 2)


    xa = array([[-5, -25, pi/3, 15, 0.1]]).T
    xb = array([[20, -15, pi/4, 18, 0.2]]).T
    
    
    zhat = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]).T
    Gz = 1e3 * eye(6)
    Galpha_a = dt * np.diag([0.1, 0.1, 0.5])
    Galpha_b = dt * np.diag([0.1, 0.1, 0.5])
    Galpha = block_diag(Galpha_a, Galpha_b)
    
    for t in arange(0,10,dt) :   
        clear(ax)
        draw_car(xa)
        draw_car(xb)
        scatter(La[0], La[1])
    
        Ck, yk, Gbetak = gall(xa, xb)
        
        Aak = np.array([[1.0, 0.0, dt*np.cos(xa[4,0])*np.cos(xa[2,0])],
                        [0.0, 1.0, dt*np.cos(xa[4,0])*np.sin(xa[2,0])],
                        [0.0, 0.0, 1.0]])
        Abk = np.array([[1.0, 0.0, dt*np.cos(xb[4,0])*np.cos(xb[2,0])],
                        [0.0, 1.0, dt*np.cos(xb[4,0])*np.sin(xb[2,0])],
                        [0.0, 0.0, 1.0]])
        Ak = block_diag(Aak, Abk)
                        
        uk = np.array([[0.0, 0.0, dt*ua[0,0], 0.0, 0.0, dt*ub[0, 0]]]).T
        
        zhat, Gz = kalman(zhat, Gz, uk, yk, Galpha, Gbetak, Ak, Ck)
        draw_ellipse(zhat[:2,0], Gz[:2, :2], 0.9, "green", 2)
        draw_ellipse(zhat[3:5,0], Gz[3:5, 3:5], 0.9, "green", 2)
        
        alpha_a = xa*0
        alpha_a[[0, 1, 3], 0] += mvnrnd1(Galpha_a).flatten()
        alpha_b = xb*0
        alpha_b[[0, 1, 3], 0] += mvnrnd1(Galpha_b).flatten()

        xa = xa + dt*f(xa,ua) + alpha_a
        xb = xb + dt*f(xb,ub) + alpha_b

# one_car()    
two_cars()    
       
