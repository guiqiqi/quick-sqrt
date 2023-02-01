#include <math.h>
#include <stdio.h>
#include <stdlib.h>


double isqrt(double x) {
    double a = x;
    unsigned long *exponent = (unsigned long *)&x;
    *(exponent) = (*exponent + 0x3feea66216141ec8) >> 1;
    x = (x + a / x) / 2;
    return x;
}

int main(int argc, const char *argv[]) {
    if (argc != 2) exit(1);
    char* ptr;
    double x = strtod(argv[1], &ptr);
    double sqrted = isqrt(x);
    printf("error: %f\n", sqrted - sqrt(x));
    return 0;
}
