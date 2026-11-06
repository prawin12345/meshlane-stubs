from ..__about__ import __version__ as __version__
from .._common import num_nodes_per_cell as num_nodes_per_cell, warn as warn
from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

nastran_to_meshio_type: Incomplete
nastran_solid_types: Incomplete
meshio_to_nastran_type: Incomplete

def read(filename): ...
def read_buffer(f): ...
def write(filename, mesh, point_format: str = 'fixed-large', cell_format: str = 'fixed-small') -> None: ...
