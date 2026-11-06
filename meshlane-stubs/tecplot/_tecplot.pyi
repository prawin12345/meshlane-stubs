from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh
from _typeshed import Incomplete

zone_key_to_type: Incomplete
tecplot_to_meshio_type: Incomplete
meshio_to_tecplot_type: Incomplete
meshio_only: Incomplete
meshio_to_tecplot_order: Incomplete
meshio_to_tecplot_order_2: Incomplete
meshio_type_to_ndim: Incomplete

def read(filename): ...
def readline(f): ...
def read_buffer(f): ...
def write(filename, mesh) -> None: ...
