from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh
from _typeshed import Incomplete

meshio_only: Incomplete
numnodes_to_meshio_type: Incomplete
meshio_to_flac3d_type: Incomplete
flac3d_to_meshio_order: Incomplete
meshio_to_flac3d_order: Incomplete
meshio_to_flac3d_order_2: Incomplete
flag_to_numdim: Incomplete

def read(filename):
    """Read FLAC3D f3grid grid file."""
def read_buffer(f, binary):
    """Read binary or ASCII file."""
def split_f_z(mesh): ...
def write(filename, mesh: Mesh, float_fmt: str = '.16e', binary: bool = False):
    """Write FLAC3D f3grid grid file."""
