from ..__about__ import __version__ as __version__
from .._common import info as info, join_strings as join_strings, raw_from_cell_data as raw_from_cell_data, replace_space as replace_space, warn as warn
from .._exceptions import CorruptionError as CorruptionError, ReadError as ReadError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from .._vtk_common import meshio_to_vtk_order as meshio_to_vtk_order, meshio_to_vtk_type as meshio_to_vtk_type, vtk_cells_from_data as vtk_cells_from_data
from _typeshed import Incomplete

def num_bytes_to_num_base64_chars(num_bytes): ...
def get_grid(root): ...

vtu_to_numpy_type: Incomplete
numpy_to_vtu_type: Incomplete

class VtuReader:
    """Helper class for reading VTU files. Some properties are global to the file (e.g.,
    byte_order), and instead of passing around these parameters, make them properties of
    this class.
    """
    compression: Incomplete
    header_type: Incomplete
    byte_order: Incomplete
    points: Incomplete
    point_data: Incomplete
    field_data: Incomplete
    def __init__(self, filename) -> None: ...
    def read_uncompressed_binary(self, data, dtype): ...
    def read_compressed_binary(self, data, dtype): ...
    def read_data(self, c): ...

def read(filename): ...
def write(filename, mesh, binary: bool = True, compression: str = 'zlib', header_type=None): ...
