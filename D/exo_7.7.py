from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

y = array([8.0, 7.0, 0.0]).T
C = array([[2.0, 3.0],
           [3.0, 2.0],
           [1.0, -1.0]])
xbar = array([0.0, 0.0]).T
Gx = np.eye(2) * 1e5

ybar = C @ xbar

ytilde = y - C @ xbar

Gbeta = np.diag([1.0, 4.0, 4.0])
Gy = C @ Gx @ C.T + Gbeta

print("Gy = \n", Gy)

K = Gx @ C.T @ np.linalg.inv(Gy)
print("Kalman gain = \n", K)

xhat = xbar + K @ ytilde
print("xhat = \n", xhat)

Geps = Gx - K @ C @ Gx

print("Geps = \n", Geps)

yhat = C @ xhat

print("yhat = \n", yhat)

r = y - yhat
print("r = \n", r)