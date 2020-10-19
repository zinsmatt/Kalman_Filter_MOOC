from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

    
tmax=100 
ax=init_figure(0,tmax,-10,10)
δ=0.1 
T=arange(0,tmax,δ) 
kmax=size(T)
X=randn(1,kmax)
X=X.flatten()
plot(T, X, 'red')
pause(1)



