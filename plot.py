import matplotlib.pyplot as plt
import numpy

from magic import ErrorFunction, const

if __name__ == "__main__":
    numbers = numpy.arange(0, 10000, 0.1)
    error = ErrorFunction(numbers, 1000)
    gap = 2**40
    magics = numpy.arange(const.MagicStart, const.MagicEnd, gap, dtype=numpy.uint64)

    # Plot diff
    diff = error.batch(magics)
    plt.figure(1)
    plt.plot(magics, diff)
    plt.ylabel("Error")
    plt.xticks(
        (const.MagicStart, const.MagicEnd),
        (f"{const.MagicStart:x}", f"{const.MagicEnd:x}"),
    )

    # Plot derivative
    ds = error.ds(magics)
    plt.figure(2)
    plt.plot(magics, ds)
    plt.ylabel("Derivative")
    plt.xticks(
        (const.MagicStart, const.MagicEnd),
        (f"{const.MagicStart:x}", f"{const.MagicEnd:x}"),
    )

    plt.show()
