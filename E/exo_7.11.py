from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
# ax=init_figure(-30,30,-30,30)
# C = array([[1,1]])
# y = 3
# Gbeta = 1
# x0 = array([[0],[0]])
# G0 = array([[100,0],[0,100]]) 

# draw_ellipse(x0,G0,0.9,ax,[0.8,0.8,1])
# pause(1.0)

# xup,Gup = kalman_correc(x0,G0,y,Gbeta,C)

# draw_ellipse(xup,Gup,0.9,ax,[1,0.8,0.8])
# pause(1.0)


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

def kalman(x0,Γ0,u,y,Γα,Γβ,A,C):
    xup,Gup = kalman_correc(x0,Γ0,y,Γβ,C)
    x1,Γ1=kalman_predict(xup,Gup,u,Γα,A)
    return x1, Γ1, xup, Gup

A0 = array([[0.5, 0.0],
            [0.0, 1.0]])
A1 = array([[1.0, -1.0],
            [1.0, 1.0]])
A2 = array([[1.0, -1.0],
            [1.0, 1.0]])


u0 = array([[8.0], [16.0]])
u1 = array([[-6.0], [-18.0]])
u2 = array([[32.0], [-8.0]])

C0 = array([[1.0, 1.0]])
C1 = C0
C2 = C0

y0 = 7.0
y1 = 30.0
y2 = -6.0

Galpha = np.eye(2)
Gbeta = 1.0

xhat0 = array([[0.0], [0.0]])
Gx0 = np.eye(2) * 100
draw_ellipse(xhat0, Gx0, 0.9, "black", 4)

xhat1, Gx1, xup0, Gup0 = kalman(xhat0, Gx0, u0, y0, Galpha, Gbeta, A0, C0)
print("xhat1 = \n", xhat1)
print("Gx1  = \n", Gx1)
draw_ellipse(xup0, Gup0, 0.9, "black", 2)
draw_ellipse(xhat1, Gx1, 0.9, "red", 4)
xhat2, Gx2, xup1, Gup1 = kalman(xhat1, Gx1, u1, y1, Galpha, Gbeta, A1, C1)
draw_ellipse(xup1, Gup1, 0.9, "red", 2)
draw_ellipse(xhat2, Gx2, 0.9, "green", 4)
xhat3, Gx3, xup2, Gup2 = kalman(xhat2, Gx2, u2, y2, Galpha, Gbeta, A2, C2)
draw_ellipse(xup2, Gup2, 0.9, "green", 2)
draw_ellipse(xhat3, Gx3, 0.9, "magenta", 4)