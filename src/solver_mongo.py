#!/usr/bin/env python2.7

from pymongo import MongoClient
import pymongo.errors
import bson
import cPickle as pickle
import solver
import numpy as np

# Connexion a la base de donnees mongoDB
username, password, host, dbname = 'user', 'user123', '127.0.0.1', 'dinghao'
client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))
db = client.dinghao

# Recuperer l'id des inputs pour l'initialisation du calcul
init_id = raw_input("Entrer l'id de l'init : ") or "5b1085116e955233e756b33d"
print init_id

# Recuperer les donnees necessaires au calcul
data = db['init'].find_one({'_id': bson.objectid.ObjectId(init_id)})

dt = data["dt"]
dx = data["dx"]
dy = data["dy"]
Nt = data["Nt"]
tf = data["tf"]
Nt_0 = data['num_run']
solver_type = str(data["solver_algo"])
V = np.array( pickle.loads(data["V"]) , order="F" )
t = np.linspace(0, tf, Nt, dtype=np.float32)

run = db['run'].find_one({'init_id': bson.objectid.ObjectId(init_id)}, sort= [('t', -1)])

psi0 =  np.array( pickle.loads(run["psi"]) , order="F", dtype="complex128")
norm = np.linalg.norm(psi0, ord=1)

# Initialisation du solver
sol = solver.Solver(str(solver_type), psi0, V, 6.582119514, 939.5654133, dt, dx, dy)

# Calcul de la solution de schrodinger 2D dependant du temps
try:
    for it in range(Nt_0,Nt):
        for i in range (2000):
            if (solver_type == "ftcs"):
                psi = sol.ftcs()
            elif (solver_type == "btcs"):
                psi = sol.btcs(50)
            else:
                psi = sol.ctcs(50)
            psi = np.array( sol.ftcs(), order="F", dtype="complex128" ) 
            N = np.abs(psi)/ norm
        bindat = bson.binary.Binary(pickle.dumps(psi, protocol = 2))
        psi_id = db['run'].insert_one({
            'psi': bindat
        }).inserted_id
        db['run'].update_one({'_id': psi_id}, {'$set': {'t': 0, 'init_id': bson.objectid.ObjectId(init_id), 'norm': np.linalg.norm(psi, ord=1)}})
        result = db['init'].update_one({'_id': bson.objectid.ObjectId(init_id)}, {'$inc': {'num_run': 1}})
        print("Iter %s / %s, t = %s" % (str(it + 1), str(Nt), str(t[it])))
        
except pymongo.errors.OperationFailure as e:
  print("ERROR: %s" % (e))