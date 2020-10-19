from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py
A = array([[2,1],[15,5],[3,12]])    
B = array([[15,5],[3,12],[2,1]])    
xhat = array([[1,2]]).T
Γx = 100*eye(2)
Γβ = 1
ax=init_figure(-5,20,-5,20)
for i in range(3):  
    pause(0.5)  
    a,b = A[i],B[i]
    plot([a[0],b[0]],[a[1],b[1]],color="black")    
draw_disk(xhat,0.5,ax,"blue")
pause(1)