#!/usr/bin/env python

# coding=utf-8
import numpy as np
import cPickle as pickle
import pprint, scipy, math
import math
from numpy.polynomial.hermite import Hermite

def integral(mat ,dx, dy, Nx, Ny):
    S = 0
    V = 0
    for i in range(0,Nx-1):
        for j in range(0,Ny-1):
            V += dy * dx * (mat[i][j]+mat[i][j+1]+mat[i+1][j]+mat[i+1][j+1]) / 4 

    return V

# fonction pour calculer les fonctions d'onde
def ho_evec(x,n):
    # Les constantes
    m = 6.582119514
    w = 1
    h = 939.5654133
    vec = [0]*9
    vec[n] = 1
    Hn = Hermite(vec)
    ohm = m * w / h
    f1 = (1/math.sqrt(2**n * math.factorial(n)))
    f2 = pow(m*ohm/math.pi,0.25)
    f3 = np.exp(-0.5 * m * ohm * x**2)
    f4 = Hn(x*math.sqrt(m*ohm))
    return f1 * f2 * f3 * f4

def gaussian_2d(X, Y, sigX, sigY, muX, muY):
    return np.exp(-(np.power(X - muX,2)/(sigX*sigX) + np.power(Y-muY,2)/(sigY*sigY)))

def calc_oh(x, y, nx, ny):
    psi =  ho_evec(x, nx).reshape(1, x.size) * ho_evec(y, ny).reshape(y.size, 1)
    return psi

def calc_onde_plane(X, Y, kx = 1, ky = 1, w = 1, t = 0, phase = 0, muX = 0, muY = 0, sigX = 1, sigY = 1):
    psi = np.exp(1j* (kx*X + ky*Y -w*t + phase))
    return psi *  gaussian_2d(X, Y, sigX, sigY, muX, muY)