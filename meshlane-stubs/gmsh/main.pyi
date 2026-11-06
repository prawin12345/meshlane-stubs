from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from os import PathLike
from typing import IO, Protocol

class Reader(Protocol):
    @staticmethod
    def read_buffer(f: IO[bytes], is_ascii: bool, data_size: int) -> Mesh: ...

class Writer(Protocol):
    @staticmethod
    def write(filename: str | PathLike[str], mesh: Mesh, float_fmt: str = '', binary: bool = True): ...

def read(filename: str | PathLike[str]) -> Mesh:
    """Reads a Gmsh msh file."""
def read_buffer(f: IO[bytes]) -> Mesh: ...
def write(filename: str | PathLike[str], mesh: Mesh, fmt_version: str = '4.1', binary: bool = True, float_fmt: str = '.16e') -> None:
    """Writes a Gmsh msh file."""
