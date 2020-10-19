from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
pv=array([[sqrt(2)],[-1],[1]])
print(pv)
t = array([[-3],[-1],[0],[2],[3],[6]])
yv=pv[0,0]*t*t+pv[1,0]*t+pv[2,0]
y=round(yv)
print(y)
plot(t,y,color="black")
plot(t,yv,color="red")
        

