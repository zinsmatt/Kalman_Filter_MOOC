
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


xhat = array([[0,1]]).T
Gx = np.diag([0, 0.02**2])
Galpha = np.diag([0.0, 0.01**2])

# ax = init_figure(-1,12,-1,2)
# clear(ax)

draw_ellipse(xhat, Gx, 0.99, "red", 2)


ex1 = [0] * 21
deter = [0] * 21
deter[0] = np.linalg.det(Gx)


for k in range(20):
    u = 1 if k < 10 else -1
    Ak = np.array([[1.0, u],
                   [0.0, 1.0]])
    xhat, Gx = kalman(xhat, Gx, np.zeros((2, 1)), np.zeros((0, 1)), Galpha, np.zeros((0,1)), Ak, np.zeros((0, 2)))
    draw_ellipse(xhat, Gx, 0.99, "blue", 1)
    ex1[k+1] = np.sqrt(Gx[0, 0])
    deter[k+1] = np.linalg.det(Gx)

plt.figure("Ecart type de la position")
plt.plot(ex1)
# L'incertitude sur la position baisse entre k = 10 et k = 15. On peut le voir par la projection des ellipses sur x1.


plt.figure("Determinant de Gx")
plt.plot(deter)

# Le determinant represente le volume de l'incertitude. Cette incertitude ne fait qu'augmenter au cours du temps,
# même si sa projection sur x1 baisse à un moment.