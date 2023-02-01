static unsigned long _magic = 0x3feea66216141ec8;

double sqrt(double x) {
    double a = x;

    // Fast approach to root by dividing the exponent part by 2
    unsigned long *exponent = (unsigned long *)&x;
    *(exponent) = (*exponent + _magic) >> 1;

    // Newton iteration
    x = (x + a / x) / 2;
    return x;
}

void sqrts(double *x, double *y, unsigned int size) {
    for (unsigned int index = 0; index < size; ++index)
        y[index] = sqrt(x[index]);
}

void set_magic(unsigned long n) {
    _magic = n;
}
