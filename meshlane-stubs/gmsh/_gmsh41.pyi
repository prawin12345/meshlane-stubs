import numpy as np
from .._common import cell_data_from_raw as cell_data_from_raw, num_nodes_per_cell as num_nodes_per_cell, raw_from_cell_data as raw_from_cell_data, warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from os import PathLike
from typing import Any, IO

c_int: np.dtype[np.int32]
c_size_t: np.dtype[Any]
c_double: np.dtype[np.float64]

def read_buffer(f: IO[bytes], is_ascii: bool, data_size: int) -> Mesh: ...
def write(filename: str | PathLike[str], mesh: Mesh, float_fmt: str = '.16e', binary: bool = True):
    """Writes msh files, cf.
    <http://gmsh.info/doc/texinfo/gmsh.html#MSH-file-format>.
    """
