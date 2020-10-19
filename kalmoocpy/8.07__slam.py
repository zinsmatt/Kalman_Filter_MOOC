
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

D=loadcsv("slam_data.csv")
t,φ,θ,ψ,vr,pz,a = D[:,0],D[:,1],D[:,2],D[:,3],D[:,4:7].T,D[:,7],D[:,8]


xhat = zeros((15,1))
dt = 0.1
Gx = diag([0,0,0,1,1,1,1,1,1,1,1,1,1,1,1])*10**6
Galpha = diag([0.01,0.01,0.01,0,0,0,0,0,0,0,0,0,0,0,0])
A = eye(15)

def g(i):
    T = array([[10540,10920,13740,17480,30380,36880,40240,48170,51720,52320,52790,56880],
               [1,2,1,0,1,5,4,3,3,4,5,1],
                [52.42,12.47,54.40,52.68,27.73,26.98,37.90,36.71,37.37,31.03,33.51,15.05]])
    y = array([[pz[i]]])
    C = array([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]])
    Gbeta = 0.1*eye(1)
    if i in T[0]:
        j = list(T[0]).index(i)
        k,rk = T[1,j],T[2,j]
        yi = R@array([[0,-sqrt(rk**2-a[i]**2),-a[i]]]).T
        y = vstack((yi[0:2,:],y))
        Ci = hstack( (eye(2,3), zeros((2,2*k)), -eye(2), zeros((2,12-2*(k+1)))))
        C = vstack((Ci,C))
        Gbeta = 0.1*eye(3)
    return y, C, Gbeta


ax=init_figure(-200,900,-300,800)
N=len(t)


for i in range(N):
    R = eulermat(φ[i],θ[i],ψ[i])
    v = vr[:,i].reshape(3,1)
    u = vstack((dt*R@v, zeros((12,1))))
    y, C, Gbeta = g(i)
    xhat,Gx = kalman_predict(xhat,Gx,u,Galpha,A)
    if i%300 == 0:
        draw_ellipse(xhat[0:2],Gx[0:2,0:2],0.99,ax,[0.4,0.4,1])
        pause(0.01)
