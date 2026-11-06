from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh

def read(filename): ...
def write(filename, mesh, float_fmt: str = '.16e'): ...
