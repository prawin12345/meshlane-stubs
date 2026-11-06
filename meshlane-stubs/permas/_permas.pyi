from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

permas_to_meshio_type: Incomplete
meshio_to_permas_type: Incomplete

def read(filename):
    """Reads a PERMAS dat file."""
def read_buffer(f): ...
def get_param_map(word, required_keys=None):
    """
    get the optional arguments on a line

    Example
    -------
    >>> iline = 0
    >>> word = 'elset,instance=dummy2,generate'
    >>> params = get_param_map(iline, word, required_keys=['instance'])
    params = {
        'elset' : None,
        'instance' : 'dummy2,
        'generate' : None,
    }
    """
def read_set(f, params_map): ...
def write(filename, mesh) -> None: ...
