
import numpy
from magic import lib

start, stop = 0, 10000
delta = 0.001
dataset = numpy.arange(start=start, stop=stop, dtype=numpy.double)

lib.set_magic(0x3feea66216141ec8)

correct = numpy.sqrt(dataset)
result = numpy.zeros(dataset.size, dtype=numpy.double)
lib.sqrts(dataset, result)
print(numpy.sum(correct - result) / dataset.size)
