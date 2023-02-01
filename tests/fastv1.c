#include <stdio.h>
#define EPSILON 1e-14

static unsigned int count = 0;

double iabs(double x) { return x >= 0 ? x : -x; }

double isqrt(double x) {
    double a = x;
    double guess = 0;
    unsigned long *exponent = (unsigned long *)&x;
    *(exponent) = (*exponent + 0x3ff0000000000000) >> 1;
    count = 0;
    while (iabs(guess - x) > EPSILON) {
        guess = x;
        x = (x + a / x) / 2;
        count++;
    }
    return x;
}

int main() {
    for (int x = 1; x < 1000000000; x *= 10)
        printf("sqrt(%d) = %f - %d iters\n", x, isqrt(x), count);
    return 0;
}
