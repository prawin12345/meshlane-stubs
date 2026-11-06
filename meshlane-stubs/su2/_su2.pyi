from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

su2_type_to_numnodes: Incomplete
su2_to_meshio_type: Incomplete
meshio_to_su2_type: Incomplete

def read(filename): ...
def read_buffer(f): ...
def read_multi(filename):
    """Read every zone of a (multi-zone) SU2 file.

    Returns ``(meshes, names)``: one :class:`Mesh` per ``IZONE`` section, and the
    zone names (``zone_<i>``, or the names ``write_multi`` stored).
    """
def write(filename, mesh, float_fmt: str = '.17g') -> None: ...
def write_multi(filename, meshes, mesh_names=None, float_fmt: str = '.17g', **kwargs) -> None:
    """Write several meshes as the zones of a multi-zone SU2 file.

    The zone names (``mesh_names``) are stored in comments, which SU2 ignores,
    so that ``read_multi`` gives them back.
    """
