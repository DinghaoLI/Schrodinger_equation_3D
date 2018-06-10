/**
 *@file main.cpp
 */

#include <fstream>
#include <armadillo>
#include "time.h"
#include "Solver.h"

/**
 * @mainpage Calcul et tracé de l'Equation de Schrödinger non relativiste dépendant du temps
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

/**
 *La fonction principale
 *
 *Cette fonction a pour but de calculer les données nécessaires pour tracer les grraphes
 *
 *@return la fonction créer des fichier .txt et retourne 0
 */

int main()
{
    arma::mat A = arma::zeros(2,2);
    arma::mat B = arma::ones(2,2);
    arma::cx_mat C1 = arma::cx_mat(A,B);
    arma::cx_mat C2 = arma::cx_mat(B,A);

    Solver s = Solver(C1, A, 1, 1, 0.1, 0.1,0.1);
    std::cout<< s.ftcs() <<std::endl;
    Solver s1 = Solver(C1, A, 1, 1, 0.01, 0.1,0.1);
    std::cout<< s1.ftcs() <<std::endl;
    Solver s2 = Solver(C1, A, 1, 1, 0.001, 0.1,0.1);
    std::cout<< s2.ftcs() <<std::endl;
    Solver s3 = Solver(C1, A, 1, 1, 0.0001, 0.1,0.1);
    std::cout<< s3.ftcs() <<std::endl;
    return 0;
}


