from roblib import *  # available at https://www.ensta-bretagne.fr/jaulin/roblib.py



M = np.array([[1, 0, -1, 1],
              [2, 1, 1, -1],
              [-3, 2, -1, 1],
              [-7, -3, 1, -1],
              [-11, -7, -1, 1],
              [-16, -11, 1, -1]], dtype=float)
y = np.array([-2, 3, 7, 11, 16, 36], dtype=float)

print("rank M ", np.linalg.matrix_rank(M))
# p_hat = np.linalg.inv(M.T @ M) @ M.T @ y # erreur M est de rang 3 donc M.T@M n'est pas inversible.
# Les entrées données ne permettent pas d'estimer les paramètres.

# autres entrées
M = np.array([[1, 0, -1, -2],
              [2, 1, 1, -1],
              [-3, 2, -1, 1],
              [-7, -3, 1, -1],
              [-11, -7, -1, 1],
              [-16, -11, 1, -1]], dtype=float)

p_hat = np.linalg.inv(M.T @ M) @ M.T @ y
print("parametres estimés: ", p_hat)
