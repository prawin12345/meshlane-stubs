from .._exceptions import ReadError as ReadError
from _typeshed import Incomplete

NODE: int
MIXED: int
PYRA_13: int
NGON_n: int
NFACE_n: int
TYPES: Incomplete
NAMES: Incomplete
PERMUTATIONS: Incomplete

def type_name(code): ...
def renumber(code, version):
    """Element type code in the current numbering, for a file of this version."""
def nodes_per_element(code): ...
def ragged(connectivity, num_elements, offsets):
    """CSR (ptr, values) of an NGON_n or NFACE_n section: CGNS 4 stores the
    offsets in ElementStartOffset, older files put each element's length in
    front of its values."""
def split_mixed(connectivity, num_elements, offsets, version):
    """Split a MIXED section by element type.

    Returns ``{code: (local element indices, nodes (n, k))}``, where code is the
    element type in the current numbering, or NGON_n + k for polygons."""
def to_meshlane(code, nodes):
    """meshlane (cell type, nodes) of elements of a fixed CGNS type; nodes are
    still 1-based."""
