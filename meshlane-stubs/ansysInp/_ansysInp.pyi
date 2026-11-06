from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh, topological_dimension as topological_dimension

def read(filename): ...
def write(filename, mesh) -> None: ...
