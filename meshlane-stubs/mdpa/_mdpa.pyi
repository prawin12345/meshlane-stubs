from .._common import num_nodes_per_cell as num_nodes_per_cell, raw_from_cell_data as raw_from_cell_data, warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh
from _typeshed import Incomplete

inverse_num_nodes_per_cell: Incomplete
local_dimension_types: Incomplete

def read(filename):
    """Reads a KratosMultiphysics mdpa file."""
def read_buffer(f): ...
def cell_data_from_raw(cells, cell_data_raw): ...
def write(filename, mesh, float_fmt: str = '.16e', binary: bool = False) -> None:
    """Writes mdpa files, cf.
    <https://github.com/KratosMultiphysics/Kratos/wiki/Input-data>.
    """
