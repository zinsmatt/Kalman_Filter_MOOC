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
    pts += c.reshape((2, 1))
    plot2D(pts, col, 1)


N = 1000
X = randn(2, N)

ax = init_figure(-10, 10, -10, 10)

# 1)
plt.scatter(X[0, :], X[1, :], s=0.5)


# 2)
xbar = array([[1],[2]])
Gx = array([[3, 1],
            [1, 3]])

X2 = sqrtm(Gx) @ X + xbar
plt.scatter(X2[0, :], X2[1, :], s=0.5, color='red')

draw_ellipse(xbar, Gx, 0.9, "red")
draw_ellipse(xbar, Gx, 0.99, "blue")
draw_ellipse(xbar, Gx, 0.999, "green")

# 3)
xbar_est = np.mean(X2, axis=1).reshape((2, 1))
Gx_est = (1 / N ) * (X2 - xbar_est) @ (X2 - xbar_est).T

#%%





# 4) et 5)
ax = init_figure(-10, 10, -10, 10)

dt = 0.01
A = np.array([[0.0, 1.0],
              [-1.0, 0.0]])
B = np.array(([2.0], [3.0]))

Ad = np.eye(2) + A *dt
x = X2
for t in np.arange(0, 5, dt):
    ud = B * dt * np.sin(t)

    x = Ad @ x + ud

    xbar = Ad @ xbar + ud
    Gx = Ad @ Gx @ Ad.T

    plt.clf()
    plt.scatter(x[0, :], x[1, :], s=1)
    draw_ellipse(xbar, Gx, 0.9, "red")
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.show()
    pause(0.00001)