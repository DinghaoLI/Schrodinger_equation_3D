#!/usr/bin/env python2.7
import solver
import numpy as np
import cPickle as pickle
import pprint, scipy, math
import math
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import Hermite
from scipy.integrate import dblquad 
from functools import partial

def integral(mat ,dx, dy, Nx, Ny):
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

def gaussian(x, mu = 0, sig = 1):
    a = 1 / (math.sqrt(2*math.pi)*sig)
    psi_x = np.exp(- 0.5* np.power((x - mu)/sig , 2.))
    return a*psi_x

def gaussian_2d(X, Y, sigX, sigY, muX, muY):
    return np.exp(-(np.power(X - muX,2)/(sigX*sigX) + np.power(Y-muY,2)/(sigY*sigY)))

def calc_oh(x, y, nx, ny):
    psi =  ho_evec(x, nx) * ho_evec(y, ny)
    return psi

def calc_oh_mat(x, y, nx, ny):
    psi =  ho_evec(x, nx).reshape(1, x.size) * ho_evec(y, ny).reshape(y.size, 1)
    return psi

def calc_onde_plane(X, Y, kx = 1, ky = 1, w = 1, t = 0, phase = 0, muX = 2, muY = 2, sigX = 1, sigY = 1):
    psi = np.exp(1j* (kx*X + ky*Y -w*t + phase))
    return psi *  gaussian_2d(X, Y, sigX, sigY, muX, muY)

# print dblquad(func, -1, 3, lambda x:-1, lambda x:3)

dx = .1
dy = .1
Nx = 50
Ny = 50
dt = 0.1

x = np.linspace(-5,dx*(Nx-1),Nx)
y = np.linspace(-5,dy*(Ny-1),Ny)
X,Y = np.meshgrid(x,y)

res = calc_onde_plane(X, Y)
#res = calc_oh_mat(x, y, 1, 1)

psi0 = np.array( res , order="F", dtype="complex128" ) 

V = np.array( np.zeros(psi0.shape) , order="F" ) 

type = "ftcs"

sol1 = solver.Solver( psi0, V, 6.582119514, 939.5654133, dt, dx, dy)
sol2 = solver.Solver( psi0, V, 6.582119514, 939.5654133, dt, dx, dy)
sol3 = solver.Solver( psi0, V, 6.582119514, 939.5654133, dt, dx, dy)
time = []
itg1 = []
itg2 = []
itg3 = []

print "Calculating..."

mat = psi0
matconj = psi0.conj()
psi = np.multiply(mat, matconj)
norm0 = integral(psi, dx, dy, Nx, Ny).real
time.append(0)
itg1.append(0)
itg2.append(0)
itg3.append(0)

for i in range(1, 175):
    time.append(i * dt * 10)
    for i in range(1, 10):
        mat1 = sol1.ftcs()
        mat2 = sol2.btcs(100)
        mat3 = sol3.ctcs(100)
    matconj = mat1.conj()
    psi1 = np.multiply(mat1, matconj)
    matconj = mat2.conj()
    psi2 = np.multiply(mat2, matconj)
    matconj = mat3.conj()
    psi3 = np.multiply(mat3, matconj)

    itg1.append(abs(norm0 - integral(psi1, dx, dy, Nx, Ny).real))
    itg2.append(abs(norm0 - integral(psi2, dx, dy, Nx, Ny).real))
    itg3.append(abs(norm0 - integral(psi3, dx, dy, Nx, Ny).real))

time = np.array(time)
itg1 = np.array(itg1)
itg2 = np.array(itg2)
itg3 = np.array(itg3)

plt.figure()  
p1 = plt.plot(time,itg1, label="FTCS", lw=2)
p2 = plt.plot(time,itg2, label="BTCS: iter=100", lw=2)
p3 = plt.plot(time,itg3, label="CTCS: iter=100", lw=2)
diff1 = np.max(itg1) - np.min(itg1)
diff2 = np.max(itg2) - np.min(itg2)
diff3 = np.max(itg3) - np.min(itg3)
min12 = min([np.min(itg1), np.min(itg2)])
max12 = max([np.max(itg1), np.max(itg2)])
# plt.ylim(np.min(itg1) - diff1 , np.max(itg1) + diff1)  
plt.legend()
plt.yscale('log')
plt.xlabel("time(10^-22 s)")  
plt.ylabel("Integration")  
plt.title("FTCS vs BTCS(iter=100) vs CTCS(iter=100)") 

plt.show()



