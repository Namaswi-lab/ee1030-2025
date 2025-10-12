#include <stdio.h>

void solve3x3(float A[3][3], float b[3], float x[3]) {
    float ratio;
    int i, j, k;
    float aug[3][4];

    // Build augmented matrix [A|b]
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            aug[i][j] = A[i][j];
        }
        aug[i][3] = b[i];
    }

    // Forward elimination
    for (i = 0; i < 2; i++) {
        for (j = i + 1; j < 3; j++) {
            ratio = aug[j][i] / aug[i][i];
            for (k = i; k < 4; k++) {
                aug[j][k] -= ratio * aug[i][k];
            }
        }
    }

    // Back substitution
    for (i = 2; i >= 0; i--) {
        x[i] = aug[i][3];
        for (j = i + 1; j < 3; j++) {
            x[i] -= aug[i][j] * x[j];
        }
        x[i] /= aug[i][i];
    }
}
