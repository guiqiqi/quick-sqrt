import ctypes
import os.path as path

import numpy
from numpy import ctypeslib

__all__ = ["sqrts", "sqrt", "set_magic"]

d64at = ctypeslib.ndpointer(dtype=numpy.double, ndim=1, flags="CONTIGUOUS")

_lib = ctypeslib.load_library("sqrt.dylib", path.abspath(__file__))
_sqrts, sqrt, set_magic = _lib.sqrts, _lib.sqrt, _lib.set_magic

sqrt.argtypes = (ctypes.c_double,)
sqrt.restype = ctypes.c_double
_sqrts.argtypes = (d64at, d64at, ctypes.c_uint)
_sqrts.restype = None
set_magic.argtypes = (ctypes.c_ulong,)
set_magic.restype = None


def sqrts(xs, ys):
    _sqrts(xs, ys, xs.size)
