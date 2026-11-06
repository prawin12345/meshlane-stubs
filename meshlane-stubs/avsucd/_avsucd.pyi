from .._common import warn as warn
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

meshio_to_avsucd_type: Incomplete
avsucd_to_meshio_type: Incomplete
meshio_to_avsucd_order: Incomplete
avsucd_to_meshio_order: Incomplete

def read(filename): ...
def read_buffer(f): ...
def write(filename, mesh) -> None: ...
