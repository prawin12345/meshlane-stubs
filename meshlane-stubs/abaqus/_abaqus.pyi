from ..__about__ import __version__ as __version__
from .._common import num_nodes_per_cell as num_nodes_per_cell, warn as warn
from .._exceptions import ReadError as ReadError
from .._files import is_buffer as is_buffer, open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

abaqus_to_meshio_type: Incomplete
meshio_to_abaqus_type: Incomplete

def read(filename):
    """Reads a Abaqus inp file."""
def read_buffer(f): ...
def merge(mesh, points, cells, point_sets):
    """Append an external :class:`Mesh` (from *INCLUDE) into the current
    ``points`` array and ``cells`` list, offsetting node indices."""
def get_param_map(word, required_keys=None):
    """
    get the optional arguments on a line

    Example
    -------
    >>> word = 'elset,instance=dummy2,generate'
    >>> params = get_param_map(word, required_keys=['instance'])
    params = {
        'elset' : None,
        'instance' : 'dummy2,
        'generate' : None,
    }
    """
def write(filename, mesh: Mesh, float_fmt: str = '.16e', translate_cell_names: bool = True) -> None: ...
