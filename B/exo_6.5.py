from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
import numpy as np


# 1)
P = 2 * np.random.rand(1000, 2)

y = np.array([0,1,2.65,4.885,7.646, 10.882])


epsilon = 0.5
goods = []
bads = []

for p in P:
    a, b = p
    x = np.array([[0.0],[0.0]])
    ym = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    
    A = np.array([[1.0, 0.0],
                  [a, 0.9]])
    B = np.array([[b],
                  [1.0-b]])
    C = np.array([[1.0, 1.0]])
    
    for i in range(6):
        x1 = A @ x + B
        ym[i] = C @ x
        x = x1
    

    if np.max(np.abs(ym - y)) < epsilon:
        goods.append(p)
    else:
        bads.append(p)


if len(goods):
    goods = np.vstack(goods)
    plt.scatter(goods[:, 0], goods[:, 1], color="red")
if len(bads):
    bads = np.vstack(bads)
    plt.scatter(bads[:, 0], bads[:, 1], color="blue")



# 2) 
# Transfer function
# g(z) = (10*z+b*(1+10*a)-10) / ((10*z-9)*(z-1))


# 3)
# Ensemble des solutions pour lesquelles le comportement du système reste le même.
# Cet ensemble coincide bien avec les solutions trouvées à la question 1)
a = np.linspace(0, 2, 100)
b = 7.5 / (1 + 10 * a)
plt.plot(a, b, c="green")
plt.ylim([0, 2.2])
plt.show()