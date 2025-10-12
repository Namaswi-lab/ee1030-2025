#include <stdio.h>
int main() {
    double detA = 2.0;
    int n = 2;
    double k = 2.0;
    double det2A = detA * (k * k); // Since n = 2
    printf("Determinant of 2A is: %.0lf\n", det2A);
    return 0;
}
