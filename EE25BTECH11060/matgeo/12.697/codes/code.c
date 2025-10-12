#include <stdio.h>
int main() {
    // Eigenvalues of the matrix A
    double lambda1 = 6;
    double lambda2 = -1;

    // Function f(lambda) = lambda^4 - 5*lambda^3 + 6*lambda^2 + 21
    double f_lambda1 = lambda1*lambda1*lambda1*lambda1 
                       - 5*lambda1*lambda1*lambda1 
                       + 6*lambda1*lambda1 
                       + 21;
    double f_lambda2 = lambda2*lambda2*lambda2*lambda2 
                       - 5*lambda2*lambda2*lambda2 
                       + 6*lambda2*lambda2 
                       + 21;
    // Determinant of f(A) = f(lambda1) * f(lambda2)
    double det = f_lambda1 * f_lambda2;
    printf("The determinant of A^4 - 5A^3 + 6A^2 + 21I is: %.0lf\n", det);
    return 0;
}
