from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py



# 1)
# sigma_y(t) = sqrt(delta) * sqrt(t) * sigma_x
# L'écart-type du bruit Bownien augmente en fonction de la racine carrée de t et de la racine carrée de delta.


def simu(delta, sx, tmax):
    T = arange(0, tmax, delta)     
    kmax = size(T)
    X = sx * randn(1, kmax)
    Y = np.cumsum(X) * delta
    return T, X, Y
    


tmax = 100
ax = init_figure(0,tmax,-10,10)

delta = 0.01 
sx = 1.0

T, X, Y = simu(delta, sx, tmax)

X = X.flatten()
plt.scatter(T, X, s=1, color='black')
plot(T, Y, 'red')
plt.ylim([-6, 6])
pause(1)



# on peut observer une enveloppe de la forme de la racine carrée
plt.figure()
for i in range(100):
    T, X, Y = simu(delta, sx, tmax)
    plot(T, Y, 'red')
plt.ylim([-6, 6])


# 2)
# Pour que sqrt(delta) * sigma_x = 1, il faut sigma_x = 1 / sqrt(delta)
# Cela permet de garder les mêmes propriétés statistiques, 
# même en faisant varier delta.
plt.figure()
for i in range(100):
    delta = 0.01
    T, X, Y = simu(delta, 1 / sqrt(delta), tmax)
    plot(T, Y, 'red')
plt.ylim([-20, 20])
