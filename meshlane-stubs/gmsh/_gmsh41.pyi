from .._common import cell_data_from_raw as cell_data_from_raw, num_nodes_per_cell as num_nodes_per_cell, raw_from_cell_data as raw_from_cell_data, warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

c_int: Incomplete
c_size_t: Incomplete
c_double: Incomplete

def read_buffer(f, is_ascii: bool, data_size): ...
def write(filename, mesh, float_fmt: str = '.16e', binary: bool = True) -> None:
    """Writes msh files, cf.
    <http://gmsh.info/doc/texinfo/gmsh.html#MSH-file-format>.
    """
