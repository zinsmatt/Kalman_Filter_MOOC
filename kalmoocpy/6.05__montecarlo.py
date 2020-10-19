from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

P = 2*np.random.rand(100,2)
x = array([[0],[0]])
y = array([0,1,2.5,4.1,5.8,7.5])
ym = array([0,0,0,0,0,0])
epsilon = 1

for p in P: 
   scatter(p[0], p[1],color='black')

        

