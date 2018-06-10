/**
 * @file Solver.cpp
 *
 * Fichier d'implémentation pour le calcul de la solution
 */

#include "Solver.h"


/** Constructeur des valeurs
 *
 */
Solver::Solver()
{
}

/** Constructeur des valeurs
 * @param _psi0
 * @param _V
 * @param _h
 * @param _m
 * @param _dt
 * @param _dx
 * @param _dy
 */
Solver::Solver(arma::cx_mat &_psi0, arma::mat &_V, double _h, double _m, double _dt, double _dx, double _dy){
    psi0 = _psi0;
    V = _V;
    h = _h;
    m = _m;
    dt = _dt;
    dx = _dx;
    dy = _dy;
    psi = arma::zeros<arma::cx_mat>(psi0.n_rows + 2, psi0.n_cols + 2);
    psi.submat(1,1,psi0.n_rows,psi0.n_cols) = psi0;
}


/** Calcul de solver par FTCS
 * 
 * \f[ \begin{eqnarray}\psi(t+dt) &=& \frac{ihdt}{2m}\left(\frac{\psi(x+dx)-2\psi+\psi(x-dx)}{dx^{2}} + \frac{\psi(y+dy)-2\psi+\psi(y-dy)}{dy^{2}}\right)\\
&-& \frac{idt}{h}V\psi\\
&+& \psi\end{eqnarray} 
\f]
*
* 
* @ return la fonction d'onde en t+1
 */
arma::cx_mat Solver::ftcs(){
    std::complex<double> complex_i = std::complex<double>(0.0,1.0);

    psi.submat(1,1,psi0.n_rows,psi0.n_cols) = complex_i * (h * dt)/(2* m) * ( \
        (psi.submat(2, 1, psi0.n_rows +1, psi0.n_cols) - 2.0 * psi.submat(1,1,psi0.n_rows,psi0.n_cols) + psi.submat(0, 1, psi0.n_rows -1, psi0.n_cols))/(dx*dx) \
        + (psi.submat(1,2,psi0.n_rows,psi0.n_cols +1) - 2.0 * psi.submat(1,1,psi0.n_rows,psi0.n_cols) + psi.submat(1,0,psi0.n_rows,psi0.n_cols -1))/(dy*dy) ) \
        - complex_i * dt/h * V % psi.submat(1,1,psi0.n_rows,psi0.n_cols) \
        + psi.submat(1,1,psi0.n_rows,psi0.n_cols);
    
    return psi.submat(1,1,psi0.n_rows,psi0.n_cols);
}


/** Calcul de solver par BTCS
 * 
 * 
 * \f[ \begin{eqnarray} \psi^{t+dt}=\frac{(\frac{-h^2}{2m})(\frac{\psi^{t+dt}_{x+dx}+\psi^{t+dt}_{x-dx}}{dx^2}+\frac{\psi^{t+dt}_{y+dy}+\psi^{t+dt}_{y-dy}}{dy^2})+\frac{ih}{dt}\psi^{t})}{\frac{ih}{dt}-V-\frac{h^2}{2m}(\frac{1}{dx^2}+\frac{1}{dy^2})} \end{eqnarray} 
\f]
 * @param iter
 * 
 * 
 * 
 * @return la fonction d'onde en t+1
 */
arma::cx_mat Solver::btcs(int iter){
    std::complex<double> complex_i = std::complex<double>(0.0,1.0);
    arma::cx_mat init = psi;
    arma::cx_mat tmp = psi;
    arma::cx_mat param = (-1 * V) + (complex_i * h / dt) - (h * h / m) * (1/(dx*dx) + 1/(dy*dy));  
    
    for(int i = 0; i < iter; i++){
        tmp.submat(1,1,psi0.n_rows,psi0.n_cols) = (-1 * h * h / (2*m) * \
        ((tmp.submat(2, 1, psi0.n_rows +1, psi0.n_cols) + tmp.submat(0, 1, psi0.n_rows -1, psi0.n_cols))/(dx*dx) + \
        (tmp.submat(1,2,psi0.n_rows,psi0.n_cols +1) + tmp.submat(1,0,psi0.n_rows,psi0.n_cols -1))/(dy*dy)) + complex_i * h / dt * psi.submat(1,1,psi0.n_rows,psi0.n_cols)) / param;

    }
    psi.submat(1,1,psi0.n_rows,psi0.n_cols) = tmp.submat(1,1,psi0.n_rows,psi0.n_cols);    
    return psi.submat(1,1,psi0.n_rows,psi0.n_cols);
}



/** Calcul de solver par CTCS
* 
* \f[\begin{eqnarray}\left(\frac{2i\hbar}{dt}-V(x,y)-\frac{\hbar^2}{m.dx^2}-\frac{\hbar^2}{m.dy^2}\right)\psi^{(t+dt)} &=&
\frac{-\hbar^2}{2m.dx^2}\left(\psi_{x+dx}+\psi_{x-dx}\right)\\
&-& \frac{\hbar^2}{2m.dy^2}\left(\psi_{y+dy}+\psi_{y-dy}\right)\\
&-& \frac{\hbar^2}{2m.dx^2}\left(\psi^{(t+dt)}_{x+dx}+\psi^{(t+dt)}_{x-dx}\right)\\
&-& \frac{\hbar^2}{2m.dy^2}\left(\psi^{(t+dt)}_{y+dy}+\psi^{(t+dt)}_{y-dy}\right)\\
&+& \left(V(x,y) + \frac{2i\hbar}{dt}+\frac{\hbar^2}{m.dx^2}+\frac{\hbar^2}{m.dy^2}\right)\psi
\end{eqnarray} 
\f]
*
* @param iter
*
* 
* @return la fonction d'onde en t+1
 */
arma::cx_mat Solver::ctcs(int iter){
    std::complex<double> complex_i = std::complex<double>(0.0,1.0);
    arma::cx_mat tmp = psi;
    arma::cx_mat param = (-1 * V) + (2.0*complex_i*h) / dt - (h * h)/ (m * dx * dx) - (h * h)/(m * dy*dy);  
    
    for(int i = 0; i < iter; i++){
        tmp.submat(1,1,psi0.n_rows,psi0.n_cols) = (\
        ((- h*h) / (2*m*dx*dx)) * (tmp.submat(2, 1, psi0.n_rows +1, psi0.n_cols) + tmp.submat(0, 1, psi0.n_rows -1, psi0.n_cols)) +\
        ((- h*h) / (2*m*dx*dx)) * (psi.submat(2, 1, psi0.n_rows +1, psi0.n_cols) + psi.submat(0, 1, psi0.n_rows -1, psi0.n_cols)) +\
        ((- h*h) / (2*m*dy*dy)) * (tmp.submat(1, 2, psi0.n_rows, psi0.n_cols +1) + tmp.submat(1, 0, psi0.n_rows, psi0.n_cols -1)) +\
        ((- h*h) / (2*m*dy*dy)) * (psi.submat(1, 2, psi0.n_rows, psi0.n_cols +1) + psi.submat(1, 0, psi0.n_rows, psi0.n_cols -1)) +\
        (V + (2.0*complex_i*h)/dt + (h*h)/(m*dx*dx) + (h*h)/(m*dy*dy)) % psi.submat(1,1,psi0.n_rows,psi0.n_cols)) / param;

    }
    psi = tmp;    
    return psi.submat(1,1,psi0.n_rows,psi0.n_cols);
}


