from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._exceptions import WriteError as WriteError
from _typeshed import Incomplete

FACE_TYPES: Incomplete
CELL_TYPES: Incomplete

class _Names:
    """Fluent zone names: no blanks or brackets, unique."""
    used: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, name): ...

def write(filename, mesh, binary: bool = True, zone_types=None) -> None:
    '''Write a Fluent mesh file.

    zone_types maps zone (group) names to Fluent zone types, e.g.
    ``{"inlet": "velocity-inlet", "outlet": "pressure-outlet", "plate": "solid"}``;
    boundary zones are walls and cell zones fluid otherwise.
    '''
