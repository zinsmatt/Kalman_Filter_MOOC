from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

D=loadcsv("lidar_data.csv")

n = 10

Y = D[:, 1]
Y = Y.reshape((len(Y),1))
X = D[:, 0].reshape((len(Y),1))


for i in range(X.shape[0]//n):
    Xi = X[i*n:(i+1)*n,:]
    Yi = Y[i*n:(i+1)*n,:]
    plot(Xi,Yi,color='black')
pause(1)