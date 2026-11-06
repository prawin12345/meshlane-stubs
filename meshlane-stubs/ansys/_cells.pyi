from .._exceptions import ReadError as ReadError
from _typeshed import Incomplete

class Faces:
    """Faces stored as CSR (``ptr``, ``nodes``), with the 0-based cells on either
    side (``c0``, ``c1``, -1 when there is none)."""
    ptr: Incomplete
    nodes: Incomplete
    c0: Incomplete
    c1: Incomplete
    size: Incomplete
    def __init__(self, ptr, nodes, c0, c1) -> None: ...
    def __len__(self) -> int: ...
    def subset(self, idx):
        """The faces idx, as a new Faces."""

def stored_normal_points_out_of_c0(points, faces, n_cells, sample: int = 50000):
    """Whether the right-hand normal of the stored node order points away from c0.

    Fluent writers agree on one convention per file, but it is easy to get wrong,
    so it is measured: each face votes by comparing its normal with the direction
    from the center of c0 to the face center. Only the faces of the first
    ``sample`` cells vote, which is plenty and keeps large meshes cheap."""

class _CellFaces:
    """The faces of every cell, sorted by cell then by face size, each with a flag
    telling whether its stored node order must be reversed to point outward."""
    face: Incomplete
    rev: Incomplete
    faces: Incomplete
    num: Incomplete
    offset: Incomplete
    num_tri: Incomplete
    num_quad: Incomplete
    def __init__(self, faces, n_cells, out_of_c0) -> None: ...
    def slot(self, cells, j, k):
        """Outward nodes (len(cells), k) of the j-th face of each cell, which must
        have k nodes."""
    def outward(self, cell):
        """Outward faces of one cell, as a list of node arrays."""

def build_cells(points, faces, n_cells):
    """Rebuild the cells from their faces.

    Returns ``(blocks, out_of_c0)`` where blocks is a list of
    ``(cell_type, data, cell_ids)`` (cell_ids: the 0-based Fluent cell of each row)
    and out_of_c0 is the face convention found by
    :func:`stored_normal_points_out_of_c0`.
    """
