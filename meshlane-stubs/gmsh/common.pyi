import numpy as np
from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from numpy.typing import ArrayLike as ArrayLike

c_int: np.dtype[np.int32]
c_double: np.dtype[np.float64]
