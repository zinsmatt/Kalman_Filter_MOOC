from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

xbar = array([1.0, -1.0]).T
Gx = np.eye(2, dtype=float) * 4.0


y = array([5.0, 10.0, 8.0, 14.0, 17.0]).T
C = array([[4.0, 0.0],
           [10.0, 1.0],
           [10.0, 5.0],
           [13.0, 5.0],
           [15.0, 3.0]])

Gbeta = np.eye(5, dtype=float) * 9

ytilde = y - C @ xbar

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