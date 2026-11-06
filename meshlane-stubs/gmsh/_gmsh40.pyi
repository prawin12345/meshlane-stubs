import numpy as np
from .._common import cell_data_from_raw as cell_data_from_raw, num_nodes_per_cell as num_nodes_per_cell, raw_from_cell_data as raw_from_cell_data
from .._exceptions import ReadError as ReadError
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from numpy.typing import NDArray as NDArray
from typing import IO

c_int: np.dtype[np.int32]
c_long: np.dtype[np.int32 | np.int64]
c_ulong: np.dtype[np.uint32 | np.uint64]
c_double: np.dtype[np.float64]

def read_buffer(f: IO[bytes], is_ascii: bool, data_size: int) -> Mesh: ...
def write(filename, mesh: Mesh, float_fmt: str = '.16e', binary: bool = True) -> None:
    """Writes msh files, cf.
    <http://gmsh.info//doc/texinfo/gmsh.html#MSH-ASCII-file-format>.
    """
