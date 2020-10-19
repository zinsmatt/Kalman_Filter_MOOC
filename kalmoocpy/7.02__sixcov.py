from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
θ = arange(0, 2*pi, 0.1)
x = cos(θ)
y = sin(θ)
X = array([x,y])
plot2D(X,'black',1)

A = array([[4,1],[1,3]])
B = sqrtm(A)
print("A=",A)
print("B*B=",B@B)


pause(1)