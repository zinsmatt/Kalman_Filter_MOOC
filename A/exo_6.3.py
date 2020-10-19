#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Matthieu Zins
"""
import numpy as np

U = np.array([4, 10, 10, 13, 15], dtype=float)
Tr = np.array([0, 1, 5, 5, 3], dtype=float)
Omega = np.array([5, 10, 8, 14, 17], dtype=float)

M = np.vstack((U, Tr)).T

p_hat = np.linalg.inv(M.T @ M) @ M.T @ Omega
p1 = p_hat[0]
p2 = p_hat[1]
print("p1 = %.3f, p2 = %.3f" % (p1, p2))

print("Omega2 = ", p1 * 20 + p2 * 10)