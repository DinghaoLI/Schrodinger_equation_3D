#!/usr/bin/env python2.7

import cPickle as pickle
import solver
import numpy as np
from pyevtk.hl import gridToVTK

with open('data.pickle', 'rb') as f:     
    data = pickle.load(f)

solver_type = "ftcs"
dt = data["dt"]
dx = data["dx"]
dy = data["dy"]
Nx = data["Nx"]
Ny = data["Ny"]

x = np.linspace(data["x0"],dx*(Nx-1),Nx, dtype=np.float32)
y = np.linspace(data["y0"],dy*(Ny-1),Ny, dtype=np.float32)
z = np.linspace(0.0, 1.0, 1, dtype=np.float32)
#TODO: user tf and Nt
t = np.linspace(0, 2, 60, dtype=np.float32)

save = {}
save = data
save["t"] = t
save["x"] = x
save["y"] = y
save["z"] = z
V = np.array( pickle.loads(save["V"]) , order="F" ) 
psi0 =  np.array( save["psi"] , order="F", dtype="complex128" ) 
norm = np.linalg.norm(psi0, ord=1)
save["norm"] = norm

type = "ftcs"
sol = solver.Solver(type, psi0, V, 6.582119514, 939.5654133, dt, dx, dy)
for it, vt in enumerate(t):
    print it
    print vt
    for i in range (2000):
        psi = sol.ftcs()
        N = np.abs(psi)/ norm
    save["psi_%04d" % it] = psi
    save["abs_psi%04d" % it] = N
    print('psi_%04d saved' % it)

with open('save.pickle', 'wb') as f:
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)