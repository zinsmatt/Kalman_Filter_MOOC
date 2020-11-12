from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
y = array([[0.38,3.25,4.97,-0.26]]).T
ax=init_figure(-5,40,-3,8)
p = array([3,2])
t = arange(0,20,0.1)

# ax.plot(p[0]*t - p[1]*sin(t) , p[0] - p[1]*cos(t),'green')
# pause(1)


# 1)
pbar = array([0.0, 0.0]).reshape((-1, 1))
Gp = np.eye(2) * 1e4

t = array([1.0, 2.0, 3.0, 7.0]).reshape((-1, 1))
y = array([0.38, 3.25, 4.97, -0.26]).reshape((-1, 1))

C =  np.hstack((np.ones((t.shape[0], 1)), -np.cos(t)))
print("C = \n", C)

Gbeta = 0.01 * np.eye(4)

ytilde = y - C @ pbar

Gy = C @ Gp @ C.T + Gbeta
print("Gy = \n", Gy)

K = Gp @ C.T @ np.linalg.inv(Gy)
print("Kalman gain =\n", K)

phat = pbar + K @ ytilde
print("phat = \n", phat)

Geps = Gp - K @ C @ Gp
print("Geps = \n", Geps)


# 2)
t1 = np.linspace(0.0, 10, 100)
x1 = phat[0] * t1 - phat[1] * np.sin(t1)
y1 = phat[0]  - phat[1] * np.cos(t1)
ax.plot(x1, y1, 'blue')

plt.figure()
plot(t1, y1, 'blue')
# mesures
scatter(t, y, c='red')

r = y - C @ phat
print("residus = \n", r)