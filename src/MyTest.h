// MyTest.h
#include <cxxtest/TestSuite.h>
#include "Solver.h"

class MyTestSuite1 : public CxxTest::TestSuite
{
public:

    void testSolver01(void)
    {
        double dx = 0.1;
        double dy = 0.1;
        double dt = 0.0001;

        arma::cx_mat psi0(50, 50, arma::fill::randu);
        arma::mat v(50, 50, arma::fill::randu);
        v.zeros();

        Solver solver(psi0, v, 6.582119514, 939.5654133, dt, dx, dy);
        int count = 0;
        arma::cx_mat res = solver.ftcs();
        while(count < 100){
            res = solver.ftcs();
            count++;
        }
        TS_ASSERT_DELTA(arma::norm(psi0) - arma::norm(res), 0.0, 1e-05);
    }

    void testSolver02(void)
    {
        double dx = 0.1;
        double dy = 0.1;
        double dt = 0.0001;

        arma::cx_mat psi0(50, 50, arma::fill::randu);
        arma::mat v(50, 50, arma::fill::randu);
        v.zeros();

        Solver solver(psi0, v, 6.582119514, 939.5654133, dt, dx, dy);
        int count = 0;
        arma::cx_mat res = solver.btcs(100);
        while(count < 100){
            res = solver.btcs(100);
            count++;
        }
        TS_ASSERT_DELTA(arma::norm(psi0) - arma::norm(res), 0.0, 1e-06);
    }

    void testSolver03(void)
    {
        double dx = 0.1;
        double dy = 0.1;
        double dt = 0.0001;

        arma::cx_mat psi0(50, 50, arma::fill::randu);
        arma::mat v(50, 50, arma::fill::randu);
        v.zeros();

        Solver solver(psi0, v, 6.582119514, 939.5654133, dt, dx, dy);
        int count = 0;
        arma::cx_mat res = solver.ctcs(100);
        while(count < 100){
            res = solver.ctcs(100);
            count++;
        }
        TS_ASSERT_DELTA(arma::norm(psi0) - arma::norm(res), 0.0, 1e-012);
    }
    
   
};
