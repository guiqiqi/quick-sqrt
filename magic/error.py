import numpy
import numpy.typing as npt

from . import const, lib


class ErrorFunction:
    """Error function calculation and derivative support."""

    Delta = 2**10

    def __init__(self, numbers: npt.NDArray[numpy.float64], sample_size: int) -> None:
        """
        Args:
            numbers (npt.NDArray[numpy.float64]): all possible numbers which will be used for calculating error.
            sample_size (int): each random sample size from numbers.
        """
        self._numbers = numbers
        self._sqrted = numpy.sqrt(numbers)
        self._sample_size = sample_size
        self._vectorized = numpy.vectorize(self)
        self._vectorized_d = numpy.vectorize(self.d)
        # Update cache at first time
        self.update_cache()

    def update_cache(self) -> None:
        """Update generated random cache."""
        self._indexes = numpy.random.randint(
            0, self._numbers.size - 1, size=self._sample_size
        )
        self._xs, self._ys, self._standard = (
            self._numbers[self._indexes],
            numpy.zeros(self._indexes.size),
            self._sqrted[self._indexes],
        )

    def __call__(self, magic: int) -> numpy.float64:
        """Given magic number, computes the error for each of a `sample_size` random number
        from numbers and returns the average size of the error.

        Args:
            magics (numpy.float64): magic number.
        Returns:
            numpy.float64: meaned error for magic numbers.
        """
        lib.set_magic(int(magic))
        lib.sqrts(self._xs, self._ys)
        return numpy.abs(numpy.mean(self._standard - self._ys))

    def estimate(self, magic: int, sample: int) -> numpy.float64:
        """Estimate given magic number's error."""
        self.update_cache()
        lib.set_magic(int(magic))
        lib.sqrts(self._xs, self._ys)
        return numpy.abs(numpy.mean((self._standard - self._ys) / self._standard))

    def batch(self, magics: npt.NDArray[numpy.uint64]) -> npt.NDArray[numpy.float64]:
        """Calculate batch error values."""
        self.update_cache()
        return self._vectorized(magics)

    def d(self, magic: int, delta: int = Delta, multiply: float = 1e15) -> numpy.float64:
        """Calculate derivative value of given point.
        Args:
            magics (int): magic number.
            delta: (numpy.uint64 = Delta): derivative delta size.
        Returns:
            numpy.float64: meaned error for magic numbers.
        """
        # If the left and right intervals size both greater than delta
        if const.MagicStart + delta < magic and const.MagicEnd - delta > magic:
            return multiply * (self(magic + delta) - self(magic - delta)) / (2 * delta)
        # If the left part is not enough
        if const.MagicStart + delta > magic and const.MagicEnd - delta > magic:
            return multiply * (self(magic + delta) - self(magic)) / delta
        # If the right part is not enough
        if const.MagicStart + delta < magic and const.MagicEnd - delta < magic:
            return multiply * (self(magic) - self(magic - delta)) / delta
        # For strange things, return 0
        return numpy.float64(0.0)

    def ds(self, magics: npt.NDArray[numpy.uint64]) -> npt.NDArray[numpy.float64]:
        """Calculate batch drivative."""
        self.update_cache()
        return self._vectorized_d(magics)
