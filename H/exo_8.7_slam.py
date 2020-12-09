
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_ellipse_no_fill(c, Γ, η, col, width=1):
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


def kalman_up(x0,Γ0,u,y,Γα,Γβ,A,C):
    xup,Gup = kalman_correc(x0,Γ0,y,Γβ,C)
    x1,Γ1=kalman_predict(xup,Gup,u,Γα,A)
    return(x1,Γ1,xup,Gup)     


D=loadcsv("slam_data.csv")
t,phi,theta,psi,vr,pz,a = D[:,0],D[:,1],D[:,2],D[:,3],D[:,4:7].T,D[:,7],D[:,8]


xhat = zeros((15,1))
dt = 0.1
Gx = diag([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])*10**6
Galpha = diag([0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0])
A = eye(15)




ax=init_figure(-200,900,-300,800)
N=len(t)

# 1)

# xhat = zeros((3,1))
# dt = 0.1
# Gx = diag([0,0,0])
# Galpha = diag([0.01,0.01,0.01])
# A = eye(3)

# for i in range(N):
#     R = eulermat(phi[i],theta[i],psi[i])
#     v = vr[:,i].reshape(3,1)
#     xhat += dt*R@v
#     if i%300 == 0:
#         plt.scatter(xhat[0], xhat[1], 10, "b")
#         pause(0.001)



# 2)
# G_alpha = (dt*R_k) G_alpha_v (dt*R_k).T
# G_alpha = dt*dt * G_alpha_v * R_k * R_k.T
# G_alpha = dt^2 * sigma_v^2 * I

# 3)
# G_x(t) = (t/dt) * G_alpha = t*dt*sigma_v^2*I
# sigma_x(t) = sigma_v * sqrt(t*dt)
# sigma_x(t) = 0.3 * sqrt(t)
# apres une heure de mission:
# sigma_x(3600) = 0.3 * sqrt(3600) = 18m
# apres deux heures:
# sigma_x(2*3600) = 0.3 * sqrt(2*3600) = 25m
# L'incertitude augmente avec la racine carrée du temps.

def predict():
    xhat = array([0, 0, 0])
    Gx = diag([0, 0, 0])
    Galpha = 0.01 * eye(3)
    A = eye(3)
    for i in range(N):
        uk = dt * eulermat(phi[i],theta[i],psi[i]) @ vr[:, i]
        xhat, Gx = kalman_predict(xhat, Gx, uk, Galpha, A)
        if i%300 == 0:
            draw_ellipse(xhat[:2],Gx[:2, :2],0.99,ax,[0.4,0.4,1])
            pause(0.001)
# predict()

# 4)
# Fonction d'observation
def g(i):
    T = array([[10540,10920,13740,17480,30380,36880,40240,48170,51720,52320,52790,56880],
               [1,2,1,0,1,5,4,3,3,4,5,1],
                [52.42,12.47,54.40,52.68,27.73,26.98,37.90,36.71,37.37,31.03,33.51,15.05]])
    y = array([[pz[i]]])
    C = array([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
    Gbeta = 0.01*eye(1)
    if i in T[0]:
        j = list(T[0]).index(i)
        k,rk = T[1,j],T[2,j]
        k = int(k)
        R = eulermat(phi[i], theta[i], psi[i])
        yi = R@array([[0,-sqrt(rk**2-a[i]**2),-a[i]]]).T
        y = vstack((yi[0:2,:], y))
        Ci = hstack( (eye(2,3), zeros((2,2*k)), -eye(2), zeros((2, 12-2*(k+1)))))
        C = vstack((Ci,C))
        Gbeta = diag([1.0, 1.0, 0.01])
    return y, C, Gbeta


# 5)
def filter():
    xhat = zeros((15, 1))
    Gx = diag([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])*10**6
    Galpha = diag([0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0])
    
    A = eye(15)

    for i in range(N):
        uk = dt * eulermat(phi[i],theta[i],psi[i]) @ vr[:, i]
        uk = np.vstack((uk.reshape((-1, 1)), np.zeros((12, 1))))
        y, Ck, Gbeta = g(i)
        xhat, Gx = kalman(xhat, Gx, uk, y, Galpha, Gbeta, A, Ck)
        if i%300 == 0:
            draw_ellipse_no_fill(xhat[:2, 0],Gx[:2, :2],0.9, "blue", 0.2)
            for j in range(3, len(xhat), 2):
                draw_ellipse_no_fill(xhat[j:j+2, 0], Gx[j:j+2, j:j+2], 0.9, "red")
            pause(0.001)
# filter()


# 6)
def smoother():
    x_forw = {}
    G_forw = {}
    uk = {}
    xup = {}
    Gup = {}
    x_forw[0] = zeros((15, 1))
    G_forw[0] = diag([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])*10**6
    Galpha = diag([0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0])
    A = eye(15)

    # forward
    for i in range(N):
        uk_tmp = dt * eulermat(phi[i],theta[i],psi[i]) @ vr[:, i]
        uk[i] = np.vstack((uk_tmp.reshape((-1, 1)), np.zeros((12, 1))))        
        y, Ck, Gbeta = g(i)
        x_forw[i+1], G_forw[i+1], xup[i], Gup[i] = kalman_up(x_forw[i], G_forw[i], uk[i], y, Galpha, Gbeta, A, Ck)

        if i%300 == 0:
            draw_ellipse_no_fill(x_forw[i][:2, 0],G_forw[i][:2, :2],0.9, "blue", 0.2)
            for j in range(3, len(xhat), 2):
                draw_ellipse_no_fill(x_forw[i][j:j+2, 0], G_forw[i][j:j+2, j:j+2], 0.9, "red", 0.8)
            pause(0.001)

    # backward
    x_back = {N-1:xup[N-1]}
    G_back = {N-1:Gup[N-1]}    
    for i in range(N-2, -1, -1):
        J = Gup[i] @ A.T @ np.linalg.inv(G_forw[i+1])
        x_back[i] = xup[i] + J @ (x_back[i+1]-x_forw[i+1])
        G_back[i] = Gup[i] + J @ (G_back[i+1]-G_forw[i+1]) @ J.T

        if i%300 == 0:
            draw_ellipse_no_fill(x_back[i][:2, 0],G_back[i][:2, :2],0.9, "green", 0.4)
            for j in range(3, len(xhat), 2):
                draw_ellipse_no_fill(x_back[i][j:j+2, 0], G_back[i][j:j+2, j:j+2], 0.9, "magenta", 0.8)
            pause(0.001)
smoother()