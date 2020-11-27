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

def g(x):
    g1 = norm(x[::2,:]-a)**2
    g2 = norm(x[::2,:]-b)**2
    return(array([[g1],[g2]]))
    
dt = 0.02
Galpha = diag([0,dt,0,dt])
Gbeta = eye(2) * 5
x  = array([[-2],[7],[6],[0]])
a = array([[-2,0]]).T
b = array([[4,0]]).T
Ak=array([[1,dt,0,0],[0,1-0.01*dt,0,0],[0,0,1,dt],[0,0,0,1-0.01*dt]])

xhat = array([[-1.0, 5.0, 1, 0.0]]).T
Gx = eye(4) * 10**4

ax=init_figure(-10,10,-10,10)
for ti, t in enumerate(arange(0,2,dt)):
    clear(ax)
    y = g(x) +  mvnrnd1(Gbeta)
    uk=array([[0]]*4)
    plot(a[0],a[1],'o')
    plot(b[0],b[1],'o')
    plot(x[0,0],x[2,0],'o')    
    draw_disk(a,sqrt(y[0,0]),ax,[0.8,0.8,0.8])
    draw_disk(b,sqrt(y[1,0]),ax,[0.8,0.8,0.8])   
    
    
    Ck = np.array([[2 * (xhat[0,0] - a[0, 0]), 0.0, 2*(xhat[2,0]-a[1, 0]), 0.0],
                   [2 * (xhat[0,0] - b[0, 0]), 0.0, 2*(xhat[2,0]-b[1, 0]), 0.0]])
    z = y - g(xhat) + Ck @ xhat
    
    
    xhat, Gx = kalman(xhat, Gx, 0, z, Galpha, Gbeta, Ak, Ck)
    plot(xhat[0,0],xhat[2,0],'or')
    draw_ellipse(xhat[[0, 2], 0], array([[Gx[0, 0], Gx[0, 2]],[Gx[2, 0], Gx[2, 2]]]), 0.99, "red")
    
    x = Ak @ x + mvnrnd1(Galpha)
    
    


