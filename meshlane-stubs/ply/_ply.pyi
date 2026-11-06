from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

ply_to_numpy_dtype: Incomplete
numpy_to_ply_dtype: Incomplete

def cell_type_from_count(count): ...
def read(filename): ...
def read_buffer(f): ...
def write(filename, mesh: Mesh, binary: bool = True): ...
