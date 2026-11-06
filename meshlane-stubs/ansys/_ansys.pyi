from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from ._cells import Faces as Faces, build_cells as build_cells
from ._write import write as write
from _typeshed import Incomplete

class _FluentMesh:
    """The content of a Fluent mesh, as read from a .msh or a .msh.h5 file, with
    1-based node and cell indices (0: no cell)."""
    dim: int
    nodes: Incomplete
    num_cells: int
    cell_zones: Incomplete
    listed_cells: Incomplete
    face_zones: Incomplete
    zones: Incomplete
    def __init__(self) -> None: ...
    def mesh(self): ...

class _Parser(_FluentMesh):
    buf: Incomplete
    written_by_meshlane: bool
    def __init__(self, buf) -> None: ...
    def parse(self) -> None: ...

def read(filename): ...
