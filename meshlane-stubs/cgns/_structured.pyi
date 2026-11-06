from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from ._groups import family_names as family_names, location as location
from ._tree import child as child, children as children, data as data, name as name, resolve as resolve, text as text
from _typeshed import Incomplete

def coordinates(zone, phys_dim):
    """Points of a structured zone (i fastest), rind planes removed."""

class Block:
    """Unstructured view of a structured zone."""
    zone: Incomplete
    size: Incomplete
    points: Incomplete
    stride: Incomplete
    active: Incomplete
    flipped: bool
    def __init__(self, zone, points) -> None: ...
    def cell_index(self, lo, hi):
        """Cells with lower corner in [lo, hi] (0-based, per direction)."""
    def nodes(self, lo, hi):
        """Nodes with indices in [lo, hi] (0-based, per direction)."""
    def faces(self, lo, hi):
        """Boundary faces (outward) over a node range that is flat in exactly one
        active direction, or None."""

def zone_groups(block, version):
    '''Faces generated for the BCs, and ``[(name, kind, values)]`` groups: kind
    "faces" (indices in the face block), "region points" (1-based nodes) or
    "cells" (indices of cells).'''
def interface_nodes(block):
    """Nodes on the 1-to-1 interfaces of a zone (1-based), to be merged with the
    matching nodes of the neighbouring zones."""
