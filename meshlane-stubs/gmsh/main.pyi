from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh

def read(filename):
    """Reads a Gmsh msh file."""
def read_buffer(f): ...
def write(filename, mesh, fmt_version: str = '4.1', binary: bool = True, float_fmt: str = '.16e') -> None:
    """Writes a Gmsh msh file."""
