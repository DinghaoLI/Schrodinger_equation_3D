#!/usr/bin/env python2.7

import cPickle as pickle
from schrodinger import *
from pymongo import MongoClient
import pymongo.errors
import json
import bson
import pprint, scipy, math
import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.polynomial.hermite import Hermite
from PIL import Image
import PIL.ImageOps
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# fonction pour calculer les potentiels
def calc_potentiel_null(Nx, Ny):
    return np.zeros((Nx,Ny))

def calc_potentiel_image(filename):
    img = PIL.Image.open("test.png").convert('L')
    img = PIL.ImageOps.invert(img)
    return np.array(img) * (5.0/255.0)

# definition des types d'onde et potentiels
psi_types = {"OH", "plane"}
pot_types = {"null", "img"}
solver_algos = {"ftcs", "btcs", "ctcs"}

# demander a l'utilisateur de choisir d'entrer les valeurs par console ou fichier
print "====Choissisez le mode d'initialisation console ou json==="
mode_json = raw_input("Initialiser les donnees depuis un json?(o/n)") or 'o'

if (mode_json == "o") :
    init_filename = raw_input("fichier json d'initialisation : ") or "init_data_plane.json"
    with open(init_filename, "r") as init_file :
        init_data = json.load(init_file)
    dx = init_data["dx"]
    dy = init_data["dy"]
    dt = init_data["dt"]
    Nx = init_data["Nx"]
    Ny = init_data["Ny"]
    Nt = init_data["Nt"]
    x0 = init_data["x0"]
    y0 = init_data["y0"]
    tf = init_data["tf"]
    psi_type = init_data["psi_type"]
    psi_param = init_data["psi_param"]
    pot_type = init_data["pot_type"]
    pot_param = init_data["pot_param"]
    solver_algo = init_data["solver_algo"]
    if (psi_type == "plane"):
        kx = psi_param["kx"] or 1
        ky = psi_param["ky"] or 1
        w = psi_param["w"] or 1
        muX = psi_param["muX"] or 0
        muY = psi_param["muY"] or 0
        sigX = psi_param["sigX"] or 1
        sigY = psi_param["sigY"] or 1
        phase =  psi_param["phase"] or 0
        psi_param = {"kx": kx, "ky": ky, "w": w, "phase": phase, "muX": muX,"muY": muY, "sigX": sigX, "sigY": sigY}
        print "================"
        print psi_param
    else:
        nx = psi_param["nx"] or 0
        ny = psi_param["ny"] or 0
    if (pot_type == "img"):
        filename= pot_param["filename"]

# demander a l'utilisateur d'entrer les valeurs
else :
    print "====Choisissez la dimension de la mesh==="
    defaut_mesh = raw_input("Utiliser les valeurs par defaut?(o/n)") or 'o'
    if (defaut_mesh != "o"):
        dx = raw_input("dx : ") or 0.01
        dy = raw_input("dy : ") or 0.01
        dt = raw_input("dt : ") or 0.001
        Nx = raw_input("Nx : ") or 500
        Ny = raw_input("Ny : ") or 500
        Nt = raw_input("T : ") or 100
        x0 = raw_input("x0 : ") or -30
        y0 = raw_input("y0 : ") or -30
        tf = raw_input("tf : ") or 2
    else:
        dx = .01
        dy = .01
        dt = 1
        Nx = 500
        Ny = 500
        Nt = 100
        x0= -5
        y0 = -5
        tf = 2

    psi_type = ""
    print "====Choisissez le type de fonction d'onde==="
    while (psi_type not in psi_types):
        print(psi_type, psi_types)
        psi_type = raw_input("psi_type (OH,plane): ")
        psi_type = psi_type or 'plane'

    print "====Choisissez le type de potentiel==="
    pot_type = ""
    while (pot_type not in pot_types):
        pot_type = raw_input("pot_type (null, img): ")
        pot_type = pot_type or 'null'

    print "====Entrez les parametres de la fonction d'onde===="
    if (psi_type == "plane"):
        kx = int(raw_input("kx vecteur d'onde (plane): ") or 1)
        ky = int(raw_input("ky vecteur d'onde (plane): ") or 1)
        w = int(raw_input("w pulsion (plane): ") or 1)
        muX = int(raw_input("muX moyenne (plane): ") or 0)
        muY = int(raw_input("mY moyenne (plane): ") or 0)
        sigX = int(raw_input("sigmaX (plane): ") or 1)
        sigY = int(raw_input("sigmaY (plane): ") or 1)
        phase =  int(raw_input("phase (plane): ") or 0)
        psi_param = {"kx": kx, "ky": ky, "w": w, "phase": phase, "muX": muX,"muY": muY, "sigX": sigX, "sigY": sigY}
    else:
        nx = int(raw_input("nx: ") or 0)
        ny = int(raw_input("ny: ") or 0)
        psi_param = {"nx": nx, "ny": ny}

    print "====Entrez les parametres de la potentiel===="
    if (pot_type == "img"):
        filename= raw_input("nom de fichier de l'image :")
        pot_param = {"filename": filename}

    print "====Entrez l'algorithme de solver a utiliser===="
    while (solver_algo not in solver_algos):
        solver_algo = raw_input("pot_type (ftcs, btcs, ctcs): ")
        solver_algo = solver_algo or 'null'

# demander a l'utilisateur de choisir d'entrer les valeurs par console ou fichier
print "====Activez le mode previsualisation==="
mode_plot = raw_input("Avoir un apercu de la fonction d'onde et du potentiel?(o/n)") or 'n'

V = {}
if (pot_type == "null"):
    V = calc_potentiel_null(Nx,Ny)
elif (pot_type == "img"):
    V = calc_potentiel_image(filename)
    Nx = V.shape[1]
    Ny = V.shape[0]
#plot de la potentiel
if (mode_plot == "o"):
    print x0, y0, dx,dy,Nx,Ny
    x1 = np.linspace(x0,dx*(Nx-1),Nx)
    y1 = np.linspace(y0,dy*(Ny-1),Ny)
    X1,Y1 = np.meshgrid(x1,y1)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X1, Y1, V, linewidth=0, antialiased=False, cmap=cm.viridis)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    plt.show()

# calcul des valeurs initiales
print dx,dy,Nx,Ny
x = np.linspace(x0,dx*(Nx-1),Nx)
y = np.linspace(y0,dy*(Ny-1),Ny)
X,Y = np.meshgrid(x,y)

if (psi_type == "plane"):
    psi = calc_onde_plane(X, Y, kx, ky, w, 0, phase, muX, muY, sigX, sigY)
    print np.linalg.norm(psi, ord=1)
else:
    psi = calc_oh(x, y, nx, ny)
    print np.linalg.norm(psi, ord=1)
#plot de la fonction d'onde
if (mode_plot == "o"):
    Z = np.abs(psi)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, cmap=cm.viridis)
    ax.set_xlabel('x [en fm]')
    ax.set_ylabel('y [en fm]')
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    plt.show()

# An arbitrary collection of objects supported by pickle.
data = {
    'dx': dx,
    'dy': dy,
    'dt': dt,
    'Nx': Nx,
    'Ny': Ny,
    'Nt': Nt,
    "x0": x0,
    "y0": y0,
    'tf': tf,
    'psi_type': psi_type,
    'psi_param': psi_param,
    'pot_type': pot_type,
    'pot_param': pot_param,
    "psi": bson.binary.Binary(pickle.dumps(psi, protocol = 2)),
    "V": bson.binary.Binary(pickle.dumps(V, protocol = 2))
}

print psi.shape
print V.shape

# demander a l'utilisateur de choisir d'entrer les valeurs par console ou fichier
print "====Enregistrer dans MongoDB==="

mode_mongo = raw_input("Enregistrer les donnees dans mongoDB?(o/n)") or 'n'

if (mode_mongo == 'o'):
    username, password, host, dbname = 'user', 'user123', '127.0.0.1', 'dinghao'
    client = MongoClient('mongodb://%s:%s@%s/%s' % (username, password, host, dbname))
    try:
        init_id = client['dinghao']['init'].insert_one({
            'dx': dx,
            'dy': dy,
            'dt': dt,
            'Nx': Nx,
            'Ny': Ny,
            'Nt': Nt,
            "x0": x0,
            "y0": y0,
            'tf': tf,
            'psi_type': psi_type,
            'psi_param': psi_param,
            'pot_type': pot_type,
            'pot_param': psi_param,
            "V": bson.binary.Binary(pickle.dumps(V, protocol = 2)),
            "solver_algo": solver_algo,
            "num_run": 0
            }).inserted_id
        psi_id = client['dinghao']['run'].insert_one({
            't': 0.0,
            'init_id': init_id,
            'norm': np.linalg.norm(psi, ord=1),
            'psi': bson.binary.Binary(pickle.dumps(psi, protocol = 2))
        }).inserted_id
        # creer l'index time
        if "time" not in client['dinghao']['run'].index_information():
            client['dinghao']['run'].create_index([("t", pymongo.ASCENDING), ("init_id", pymongo.ASCENDING)],name="time")
        print "Les donnees ont ete enregistrer: Veuillez conserver l'id de votre initialisation dans mongoDB"
        print("init_id: %s" % (str(init_id)))
    except pymongo.errors.OperationFailure as e:
        print("ERROR: %s" % (e))

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)