#!/usr/bin/env python2.7

import cPickle as pickle
import numpy as np
from pyevtk.hl import gridToVTK
from pymongo import MongoClient
import pymongo.errors
import bson

# Connexion a la base de donnee mongoDB
username, password, host, dbname = 'user', 'user123', '127.0.0.1', 'dinghao'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))
db = client.dinghao

# Recuperer l'id des inputs pour l'initialisation du calcul
init_id = raw_input("Entrer l'id de l'init : ") or "5b1085116e955233e756b33d"
print init_id

data = db['init'].find_one({'_id': bson.objectid.ObjectId(init_id)})

# Calcul des donnees necessaires au plot
Nx = data["Nx"]
Ny = data["Ny"]
Nt = data["Nt"]
x0 = data["x0"]
y0 = data["y0"]
dx = data["dx"]
dy = data["dy"]
tf = data["tf"]
x = np.linspace(x0,dx*(Nx-1),Nx, dtype=np.float32)
y = np.linspace(y0,dy*(Ny-1),Ny, dtype=np.float32)
z = np.linspace(0.0, 1.0, 1, dtype=np.float32)
t = np.linspace(0, tf, Nt, dtype=np.float32)

it = 0

bindat = pickle.loads(data["V"])
N = np.abs(np.array( bindat , order="F" ))
filename = 'pot'
gridToVTK(filename, x, y, z, pointData = {'N': N.astype(np.float32).reshape((Nx, Ny, 1), order = 'C')})
print('%s.vtr generated' % (filename))

# Generer les fichier VTK necessaire a l'animation
print "==== Generation des fichiers VTK===="
try:
  for run in db['run'].find({'init_id': bson.objectid.ObjectId(init_id)}, sort=[('t', 1)]):
    bindat = pickle.loads(run["psi"])
    N = np.abs(np.array( bindat , order="F" )) / run["norm"]
    filename = 'anim_plane2_%04d' % it
    gridToVTK(filename, x, y, z, pointData = {'N': N.astype(np.float32).reshape((Nx, Ny, 1), order = 'C')})
    print("Iter %s / %s, t = %s" % (str(it), str(Nt), str(t[it -1])))
    print('%s.vtr generated' % (filename))
    it+=1

except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))

print "==== Etat du calcul dans le cluster===="
print("Iter %s / %s" % (str(data["num_run"]), str(Nt)))
print("type psi: %s, type pot :%s, type algo :%s" % (data["psi_type"], data["pot_type"],data["solver_algo"] ))
print("Taille Mesh %s * %s" % (str(Nx), str(Ny)))
print("Taille Psi %s " % (str(bindat.shape)))
print("x [%s,%s]" % (str(x[0]), str(x[-1])))
print("y [%s,%s]" % (str(y[0]), str(y[-1])))
print("dx %s, dy %s" % (str(dx), str(dy)))