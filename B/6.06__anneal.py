#https://www.ensta-bretagne.fr/jaulin/robmooc.html
from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_room():
    for j in range(A.shape[1]):
        plot(array([A[0,j],B[0,j]]),array([A[1,j],B[1,j]]),color='blue')
        
def draw(p, y, col):
    draw_tank(p,'darkblue',0.1)
    p=p.flatten()
    y=y.flatten()
    for i in arange(0,8):
        plot(p[0]+array([0,y[i]*cos(p[2]+i*pi/4)]),p[1]+array([0,y[i]*sin(p[2]+i*pi/4)]),color=col)
    plt.xlim([-2, 10])
    plt.ylim([-2, 10])
    plt.show()
                
        

A=array([[0, 7, 7, 9, 9, 7, 7, 4, 2, 0,   5, 6, 6, 5],
         [0, 0, 2, 2, 4, 4, 7, 7, 5, 5,   2, 2, 3, 3]])
B=array([[7, 7, 9, 9, 7, 7, 4, 2, 0, 0,   6, 6, 5, 5],
         [0, 2, 2, 4, 4, 7, 7, 5, 5, 0,   2, 3, 3, 2]])
y=array([[6.4],[3.6],[2.3],[2.1],[1.7],[1.6],[3.0],[3.1]])                  


ax=init_figure(-2,10,-2,10)

                     
p0 = array([[1],[1],[0]]) #initial guess

    
    
def f(p):
    x, y, theta = p.flatten()
    dists = np.ones(8) * np.inf
    
    for i in range(8):
        u = np.array([[np.cos(theta + i * np.pi / 4)],
                      [np.sin(theta + i * np.pi / 4)]])
        m = np.array([x, y]).reshape((-1, 1))
        for j in range(A.shape[1]):
            a = A[:, j].reshape((-1, 1))
            b = B[:, j].reshape((-1, 1))
            if np.linalg.det(np.hstack((a-m, u))) * np.linalg.det(np.hstack((b-m, u))) < 0:
                alpha = np.linalg.det(np.hstack((a-m, b-a))) / np.linalg.det(np.hstack((u, b-a)))
                if alpha > 0:
                    dists[i] = min(dists[i], alpha)
    return dists



draw_room()
draw(p0, y, 'red')
pause(0.1)


j0 = np.sum((y - f(p0))**2)
T = 5
while T > 0.01:
    pe = p0 + T * np.random.randn(3, 1)
    je = np.linalg.norm(y.flatten() - f(pe))
    plt.clf()
    draw_room()
    draw(pe, y, 'red')
    if je < j0:
        p0 = pe
        j0 = je
    T = 0.99 * T
    pause(0.00001)