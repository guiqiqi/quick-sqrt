## Fast sqrt function using Newton's method

This project uses the Newton iterative algorithm, the gradient descent algorithm to find the magic number similar to that in "Quake 3", and implements a simple version of the fast square root algorithm.

### Usage

```bash
make && make run start=0x3fe0000000000000
```

This starts the gradient descent algorithm and solves for a relatively good "magic constant".

After testing, the absolute error of the number is about 0.013, and the relative error is about 2/10,000.

For plot error function and its derivative curve:

```bash
make plot
```

It will cost some time for calculating, in my machine with Intel i7-9750H, it costs about 7 seconds and consumped about 400MB RAM.

### Other

This repo related on Python `numpy` and `matplotlib` dependencies.

More info here (Chinese ver. Only): https://init.blog/fast-newton-sqrt