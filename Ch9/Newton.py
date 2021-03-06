# Code from Chapter 9 of Machine Learning: An Algorithmic Perspective (2nd Edition)
# by Stephen Marsland (http://stephenmonika.net)

# You are free to use, change, or redistribute the code in any way you wish for
# non-commercial purposes, but please maintain the name of the original author.
# This code comes with no warranty of any kind.

# Stephen Marsland, 2008, 2014

# Gradient Descent using Newton's method
import numpy as np


def Jacobian(x):
    # return array([.4*x[0],2*x[1]])
    return np.array([x[0], 0.4 * x[1], 1.2 * x[2]])


def Hessian(x):
    # return array([[.2,0],[0,1]])
    return np.array([[1, 0, 0], [0, 0.4, 0], [0, 0, 1.2]])


def Newton(x0):
    i = 0
    iMax = 10
    x = x0
    Delta = 1
    alpha = 1

    while i < iMax and Delta > 10 ** (-5):
        p = -np.dot(np.linalg.inv(Hessian(x)), Jacobian(x))
        xOld = x
        x = x + alpha * p
        Delta = np.sum((x - xOld) ** 2)
        i += 1
    print(x)


x0 = np.array([-2, 2, -2])
Newton(x0)
