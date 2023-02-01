import time
import argparse
import threading

import numpy
import matplotlib.pyplot as plt

from magic import ErrorFunction, const


def statistics(event: threading.Event):
    while not event.is_set():
        print(f"iter {len(error)}: error {error[-1]} at {x:x}, next {dx:f}")
        time.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        default=const.MagicStart,
        type=lambda x: int(x, 0),
        required=False,
        help="start position",
    )
    args = parser.parse_args()
    numbers = numpy.arange(0, 10000, 0.1)
    ef = ErrorFunction(numbers, 1000)

    # Statistics
    error, xs = [], []
    event = threading.Event()
    st = threading.Thread(target=statistics, daemon=True, args=(event,))

    # Gradient descent
    epsilon, lr = 1e-5, 2**32
    x = args.start
    dx = ef.d(x)
    error.append(ef(x))
    xs.append(x)
    st.start()
    while abs(dx) > epsilon:
        x -= int(dx * lr)
        dx = ef.d(x)
        error.append(ef(x))
        xs.append(x)

    # Show plot
    event.set()
    indexes = numpy.arange(len(error))
    print(f"Best magic number: {x:x} with error={ef.estimate(x, 1000)}, d={dx}")
    plt.plot(indexes, error)
    plt.show()
