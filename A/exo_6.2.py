from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py

pv = array([[sqrt(2)],[-1],[1]])

print(pv)
t = array([[-3], [-1], [0], [2], [3], [6]])
yv = pv[0, 0] * t * t + pv[1, 0] * t + pv[2, 0]
y = round(yv)
print(y)
plot(t, y, color="black")
plot(t, yv, color="red")
        
M = np.hstack((t**2, t, np.ones_like(t)))
p_hat = np.linalg.inv(M.T @ M) @ M.T @ y
print("p_hat = ", p_hat)
y_hat = M @ p_hat
print("y_hat = ", y_hat)
print("residus initiaux = ", y - yv)
print("residus filtres = ", y_hat - yv)


plt.figure()
plt.scatter(t, y, label="y", marker='+')
plt.scatter(t, y_hat, c="green", label="y_hat", marker='.')

t = np.linspace(-3, 6, 100)
yv = pv[0, 0] * t * t + pv[1, 0] * t + pv[2, 0]
plt.plot(t, yv, c="red", label="yv")

