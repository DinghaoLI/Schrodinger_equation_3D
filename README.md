# Projet IPS-PROD - ENSIIE - 2018

Calcul et tracé de la densité d'un système nucléaire

## Pré-requis

* c++ 11
* cxxtest
* python
* armadillo
* doxygen
* valgrind
* mongoDB
* paraview
* ...

## Pour compiler le code et générer la documentation

```
make
```

## Pour lancer les tests

```
make test
```

## Pour supprimer les fichiers d'exécutions

```
make clean
```

## Pour la préparation de données : FIeldGenerator

Ecrire les paramètres dans un fichier json
```
python fieldGenerator.py
```

## Pour calculer avec le solver : Solver


```
python solver_mongo.py
```

## Pour surveiller le calcul et voir les résultats : Monitor


```
make monitor.py
```

Ouvrir avec paraview les fichiers vtk générer


