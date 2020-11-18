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



# 1)

Galpha = zeros((2, 2))
A = np.eye(2)

u = 0
C0 = np.array([[2.0, 3.0]])
C1 = np.array([[3.0, 2.0]])
C2 = np.array([[1.0, -1.0]])

y0 = 8
y1 = 7
y2 = 0
xhat0 = np.array([0.0, 0.0]).reshape((-1, 1))
Gx0 = np.eye(2) * 1e3



draw_ellipse(xhat0, Gx0, 0.99, "red")
xhat1, Gx1 = kalman(xhat0, Gx0, u, y0, Galpha, 1.0, A, C0)
draw_ellipse(xhat1, Gx1, 0.99, "magenta", 2)

print("Det Gx0 = ", det(Gx0))
print("Det Gx1 = ", det(Gx1))



xhat2, Gx2 = kalman(xhat1, Gx1, u, y1, Galpha, 4.0, A, C1)
draw_ellipse(xhat2, Gx2, 0.99, "blue", 2)

xhat3, Gx3 = kalman(xhat2, Gx2, u, y2, Galpha, 4.0, A, C2)
draw_ellipse(xhat3, Gx3, 0.99, "green", 2)


print("Det Gx2 = ", det(Gx2))
print("Det Gx3 = ", det(Gx3))
print("Estimation = ", xhat3)

# 2)
y = np.array([8.0, 7.0, 0.0]).reshape((-1, 1))
Gbeta = np.diag([1.0, 4.0, 4.0])
C = np.vstack([C0, C1, C2])
xhat, Gx = kalman(xhat0, Gx0, u, y, Galpha, Gbeta, A, C)
draw_ellipse(xhat, Gx, 0.99, "yellow", 1)

print("Estimation = ", xhat)

# On obtient la même estimation lorsqu'on utilise toutes les equations en même temps.