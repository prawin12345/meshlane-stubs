from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh
from _typeshed import Incomplete

netgen_codims: Incomplete
netgen0d_to_meshio_type: Incomplete
netgen1d_to_meshio_type: Incomplete
netgen2d_to_meshio_type: Incomplete
netgen3d_to_meshio_type: Incomplete
netgen_to_meshio_type: Incomplete
netgen_to_meshio_pmap: Incomplete
meshio_to_netgen_pmap: Incomplete
n: Incomplete
ipmap: Incomplete

def read(filename): ...
def read_buffer(f): ...
def write(filename, mesh, float_fmt: str = '.16e') -> None: ...
def write_buffer(f, mesh, float_fmt) -> None: ...
