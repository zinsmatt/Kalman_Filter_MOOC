from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_ellipse(c, Γ, η, col):
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
    plot2D(pts, col, 1)



A1 = np.array([[1.0, 0.0],
               [0.0, 3.0]])
A2 = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
               [np.sin(np.pi/4), np.cos(np.pi/4)]])

G1 = np.eye(2)
G2 = 3 * np.eye(2)
G3 = A1 @ G2 @ A1.T + G1
G4 = A2 @ G3 @ A2.T
G5 = G4 + G3
G6 = A2 @ G5 @ A2.T



center = [0.0, 0.0]
draw_ellipse(center, G1, 0.9, "black")
draw_ellipse(center, G2, 0.9, "green")
draw_ellipse(center, G3, 0.9, "red")
draw_ellipse(center, G4, 0.9, "blue")
draw_ellipse(center, G5, 0.9, "magenta")
draw_ellipse(center, G6, 0.9, "black")
plt.axes().set_aspect('equal')
plt.ylim([-20, 20])
plt.xlim([-20, 20])
pause(1)