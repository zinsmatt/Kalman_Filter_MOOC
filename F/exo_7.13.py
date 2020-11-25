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


A = array([[2,1],[15,5],[3,12]])    
B = array([[15,5],[3,12],[2,1]])    

xhat0 = array([[1,2]]).T

Gx0 = 100 * eye(2)
Gbeta = eye(3)

ax=init_figure(-20,20,-20,20)

d = array([2.0, 5.0, 4.0])


U = []
Y = []
C = []
for i in range(3):  
    a,b = A[i],B[i]
    plot([a[0],b[0]],[a[1],b[1]],color="black")    
    
    u = (b - a) / np.linalg.norm(b-a)
    U.append(u)
    y = d[i] - np.cross(a, u)
    Y.append(y)  
    C.append([-u[1], u[0]])
    
U = np.vstack(U)
Y = np.vstack(Y)
C = np.vstack(C)
    
# initial state
draw_disk(xhat0,0.5,ax,"black")
draw_ellipse(xhat0, Gx0, 0.9, "black")

# correction
xhat1, Gx1 = kalman(xhat0, Gx0, 0, Y, Gx0*0, Gbeta, np.eye(2), C)


for i in range(3):
    circle = plt.Circle(xhat1, d[i], color='blue', fill=False)
    ax.add_artist(circle)

draw_disk(xhat1,0.5,ax,"green")
draw_ellipse(xhat1, Gx1, 0.9, "green")