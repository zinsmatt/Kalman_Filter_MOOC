from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

def draw_ellipse(center, G, color, p=0.9):
    s = -2 * log(1 - p)
    S, R = np.linalg.eig(G)
    a, b = sqrt(S)
    I = arange(0, 2*pi+0.1, 0.1)
    x = sqrt(s) * a * cos(I) + center[0]
    y = sqrt(s) * b * sin(I) + center[1]
    X = np.vstack((x, y))
    X = R @ X
    plot2D(X, color, 1)




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
draw_ellipse(center, G1, "black")
draw_ellipse(center, G2, "green")
draw_ellipse(center, G3, "red")
draw_ellipse(center, G4, "blue")
draw_ellipse(center, G5, "magenta")
draw_ellipse(center, G6, "black")
plt.axes().set_aspect('equal')
plt.ylim([-20, 20])
plt.xlim([-20, 20])
pause(1)