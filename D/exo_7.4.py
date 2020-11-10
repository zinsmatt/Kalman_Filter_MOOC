from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

# 1)
N = 1000
xbar = array([[1],[2]])
x = randn(2, N)
Gx = array([[3,1],[1,3]])

x = sqrtm(Gx) @ x + xbar

x_np = np.random.multivariate_normal(xbar.flatten(), Gx, (2, N))

ax=init_figure(-10,10,-10,10)

ax.scatter(x[0],x[1], s=1)
ax.scatter(x_np[0],x_np[1], c="orange", s=1)

draw_ellipse(xbar,Gx,0.9,ax,[1,0.8,0.8]) 

pause(1)


# 2)
K = Gx[0, 1] / Gx[1, 1]

x2 = np.linspace(-10, 10, 500)

x1_lin = xbar[0] + K * (x2 - xbar[1])

plt.scatter(x1_lin, x2, c="magenta", s=1)


# 3)
K = Gx[1, 0] / Gx[0, 0]
x1 = np.linspace(-10, 10, 500)

x2_lin = xbar[1] + K * (x1 - xbar[0])

plt.scatter(x1, x2_lin, c="green", s=1)

# L'estimateur de la question 2, nous donne la meilleure estimation de x1 lorsqu'on connait la valeur de x2, alors
# que l'estimateur de la question 3 donne la meilleure estimation de x2 lorsqu'on connait la valeur de x1.