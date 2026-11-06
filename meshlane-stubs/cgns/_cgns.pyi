from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from ._elements import MIXED as MIXED, NFACE_n as NFACE_n, NGON_n as NGON_n, nodes_per_element as nodes_per_element, ragged as ragged, renumber as renumber, split_mixed as split_mixed, to_meshlane as to_meshlane
from ._fields import zone_fields as zone_fields
from ._groups import boundary_conditions as boundary_conditions, family_names as family_names, subregions as subregions
from ._polyhedra import build_cells as build_cells
from ._tree import child as child, children as children, data as data, file_version as file_version, name as name, resolve as resolve, text as text
from ._write import write as write
from _typeshed import Incomplete

def read(filename): ...
def read_multi(filename):
    """Read every zone of every base as its own mesh.

    Returns ``(meshes, names)``; names are the zone names, prefixed with the base
    name when the file has several bases."""

class _Assembly:
    """Gathers the zones of a base into one mesh: points and blocks are
    concatenated, groups become point/cell sets and fields point/cell data."""
    points: Incomplete
    blocks: Incomplete
    num_points: int
    point_sets: Incomplete
    cell_sets: Incomplete
    zone_blocks: Incomplete
    point_data: Incomplete
    cell_data: Incomplete
    interface: Incomplete
    def __init__(self) -> None: ...
    def add_zone(self, zone_name, points, blocks, groups, fields, interface=None) -> None: ...
    def mesh(self, multi_zone): ...
