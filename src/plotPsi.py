#!/usr/bin/env python2.7
import solver
import schrodinger
import numpy as np
import cPickle as pickle
import pprint, scipy, math
import math
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import Hermite
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.integrate import dblquad 
from functools import partial
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


dx = .1
dy = .1
Nx = 50
Ny = 50
dt = 0.001

x = np.linspace(-5,dx*(Nx-1),Nx)
y = np.linspace(-5,dy*(Ny-1),Ny)
X,Y = np.meshgrid(x,y)

#res = schrodinger.calc_onde_plane(X, Y, kx = 1, ky = 1, w = 1, t = 0, phase = 0, muX = 2, muY = 2, sigX = 1, sigY = 1)
res = schrodinger.calc_oh(x, y, 1, 1)
psi0 = np.array( res , order="F", dtype="complex128" ) 
norm = np.linalg.norm(psi0, ord=1)
Z = np.abs(psi0) /norm
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlabel('x [en fm]')
ax.set_ylabel('y [en fm]')
surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, cmap=cm.viridis)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.show()

V = np.array( np.zeros(psi0.shape) , order="F" ) 

type = "ftcs"
sol = solver.Solver(type, psi0, V, 6.582119514, 939.5654133, dt, dx, dy)
for i in range(0, 20):
    for j in range(0,1000):
        #psi = sol.ftcs()
        #psi = sol.btcs(50)
        psi = sol.ctcs(50)
        #print psi
    Z = np.abs(psi) / norm
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('x [en fm]')
    ax.set_ylabel('y [en fm]')
    surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, cmap=cm.viridis)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    plt.show()




