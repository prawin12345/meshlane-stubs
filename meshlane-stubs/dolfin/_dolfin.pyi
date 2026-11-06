from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh

def read(filename): ...
def write(filename, mesh) -> None: ...
