#ifndef DEF_SOLVER
#define DEF_SOLVER
/**
 * @file Solver.h
 *
 * Interface de la classe Solver
 */
#include <iostream>
#include <armadillo>
#include <math.h>
#include <cmath>
#include <complex>

/**
 * @class Solver
 * 
 * ## Equation de Schrödinger non relativiste dépendant du temps
 * 
 * \f[ i\hbar\frac{\partial}{\partial t}\psi(x,y,t) = \hat{\mathcal{H}}_{(x,y)}\psi(x,y,t) \f]
 * avec l'opérateur Hamiltonien 2D :
\f[\hat{\mathcal{H}}_{(x,y)}\equiv \frac{\hat{p}_{(x)}^2}{2m} + \frac{\hat{p}_{(y)}^2}{2m} + \hat{V}(x,y),\f]
et la quantité de mouvement :
\f[\forall u \in \{x,y\},\hspace{5mm}\hat{p}_{(u)}\equiv -i\hbar\frac{\partial}{\partial u}.\f]
Constantes:
* \f$\hbar\f$ est la **constante de Planck réduite**
\f[\hbar \equiv 6.582119514\times10^{−22}\,\textrm{MeV.s}\f]
* \f$m\f$ est la **masse du neutron**
\f[m\equiv 939.5654133\,\textrm{MeV/c}^2\f]
* \f$i\f$ est le **nombre imaginaire** \f$i^2=-1\f$
 */
class Solver
{
private:
    char * solver_type;
    double h, m, dt, dx, dy;
    arma::cx_mat psi0;
    arma::mat V;

public:
    arma::cx_mat psi;
    Solver();
    Solver(arma::cx_mat &, arma::mat &, double, double, double, double, double);
    arma::cx_mat ftcs();
    arma::cx_mat btcs(int);
    arma::cx_mat ctcs(int);
};

#endif