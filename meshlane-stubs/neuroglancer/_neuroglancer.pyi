from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh

def write(filename, mesh) -> None: ...
def write_buffer(f, mesh):
    """Store a mesh in Neuroglancer pre-computed format.
    :param file: a file-like object opened in binary mode (its ``write`` method
        will be called with :class:`bytes` objects).
    :param meshlane.Mesh mesh: Mesh object to write
    """
def read(filename): ...
def read_buffer(file):
    """Load a mesh in Neuroglancer pre-computed format.
    :param file: a file-like object opened in binary mode (its ``read`` method
        is expected to return :class:`bytes` objects).
    :returns meshlane.Mesh:
    """
