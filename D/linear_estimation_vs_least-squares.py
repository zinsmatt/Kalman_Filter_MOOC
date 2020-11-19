#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 16:32:11 2020

@author: mzins
"""

import numpy as np
import matplotlib.pyplot as plt

vals = np.array([2.0, 3.0, -5.0])
x_gt = np.array([[2.0]])

C = np.array([[2],[3],[-5]])
Gx = np.array([[1000]])
Gbeta = np.eye(3)
Gy = C @ Gx @ C.T + Gbeta
K = Gx @ C.T @ np.linalg.inv(Gy)

xbar = np.array([[0.0]])

ybar = C @ xbar
beta = np.random.randn(3, 1) * 2
y = C @ x_gt + beta

xhat = xbar + K @ (y - ybar)


plt.scatter(vals, y)
plt.xlim([-10, 10])
plt.ylim([-15, 15])




values = np.linspace(-15, 15, 100)
yvalues = values * xhat.squeeze()
plt.scatter(values, yvalues, s=4, color="red")


x_est_lstsq = np.linalg.inv(C.T @ C) @ C.T @ y
yvalues_lstsq = values * x_est_lstsq.squeeze()
plt.scatter(values, yvalues, s=1, color="green")

Gxhat = Gx - K @ C @ Gx
print("Gx = ", Gx)
print("Gxhat = ", Gxhat)

#%%

import numpy as np
import matplotlib.pyplot as plt


x_gt = np.array([[2.0]])
beta = np.random.randn(4, 1) 
C = np.array([[2],[3],[-5], [8]])
y = C @ x_gt + beta
Gx = np.array([[1000]])
xbar = np.array([[0.0]])
Gbeta = np.eye(4)

for ci in range(C.shape[0]):
    Ci = C[ci].reshape((1, 1))
    Gy = Ci @ Gx @ Ci.T + 1
    K = Gx @ Ci.T @ np.linalg.inv(Gy)
    
    ybar = Ci @ xbar
    
    yi = y[ci]
    xhat = xbar + K @ (yi - ybar)
    Gxhat = Gx - K @ Ci @ Gx

    xbar = xhat
    Gx = Gxhat
    print("hxat = ", xhat)
    print("Gx = ", Gx)
    plt.figure(str(ci))
    plt.scatter(C[:ci+1], y[:ci+1])   
    plt.xlim([-10, 10])
    plt.ylim([-20, 20])

   
    values = np.linspace(-15, 15, 100)
    yvalues = values * xhat.squeeze()
    plt.scatter(values, yvalues, s=4, color="red")
    
    stddev = np.sqrt(Gx)
    print(xhat.squeeze() - stddev*3)
    print(xhat.squeeze() + stddev*3)
    yvalues_min = values * (xhat.squeeze() - stddev*3)
    yvalues_max = values * (xhat.squeeze() + stddev*3)
    plt.scatter(values, yvalues_min, s=2, color="magenta")
    plt.scatter(values, yvalues_max, s=2, color="magenta")



#%%

import numpy as np
import matplotlib.pyplot as plt

x_gt = np.array([[2.0], [1.0]])

C = np.array([[3.0, 1],
              [7  , 1],
              [-1 , 1]])

Gx = np.diag([1e5, 1e5])
Gbeta = np.eye(3)
Gy = C @ Gx @ C.T + Gbeta
K = Gx @ C.T @ np.linalg.inv(Gy)

xbar = np.array([[0.0],
                 [0.0]])

ybar = C @ xbar
beta = np.random.randn(3, 1) * 2
y = C @ x_gt + beta



xhat = xbar + K @ (y - ybar)


plt.scatter(C[:, 0], y)
plt.xlim([-10, 10])
plt.ylim([-15, 15])


values = np.linspace(-15, 15, 100)
yvalues = values * xhat[0] + xhat[1]
plt.scatter(values, yvalues, s=4, color="red")


x_est_lstsq = np.linalg.inv(C.T @ C) @ C.T @ y
yvalues_lstsq = values  * x_est_lstsq[0] + x_est_lstsq[1]
plt.scatter(values, yvalues, s=1, color="green")

print("linear estimator = ", xhat)
print("least-squares = ", x_est_lstsq)

Gxhat = Gx - K @ C @ Gx
print("Gx = ", Gx)
print("Gxhat = ", Gxhat)

