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




A = np.eye(2)
Galpha = np.zeros((2, 2))
C = np.array([[4.0, 0.0],
              [10.0, 1.0],
              [10.0, 5.0],
              [13.0, 5.0],
              [15.0, 3.0]])
y = np.array([5.0, 10.0, 11.0, 14.0, 17.0]).reshape((-1, 1))
Gbeta = 9.0

xhat0 = np.array([[1.0], [-1.0]])
Gx0 = np.diag([4.0, 4.0])
draw_ellipse(xhat0, Gx0, 0.9, "red", 2)

xhatk = xhat0
Gxk = Gx0
for k in range(y.shape[0]):
    xhatk, Gxk = kalman(xhatk, Gxk, 0, y[k], Galpha, Gbeta, A, C[k, :].reshape((1, -1)))
    draw_ellipse(xhatk, Gxk, 0.9, "blue", 1)
    
print("Estimation = \n", xhatk)
print("Covariance = \n", Gxk)