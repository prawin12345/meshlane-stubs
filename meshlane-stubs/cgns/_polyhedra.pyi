from _typeshed import Incomplete

class _CellFaces:
    """The faces of every cell, sorted by cell then by face size, each with a flag
    telling whether its stored node order must be reversed to point outward."""
    face_ptr: Incomplete
    face_nodes: Incomplete
    face_size: Incomplete
    face: Incomplete
    rev: Incomplete
    num: Incomplete
    offset: Incomplete
    num_tri: Incomplete
    num_quad: Incomplete
    def __init__(self, points, face_ptr, face_nodes, cell_ptr, cell_faces, positive) -> None: ...
    def slot(self, cells, j, k):
        """Outward nodes (len(cells), k) of the j-th face of each cell, which must
        have k nodes."""
    def outward_faces(self):
        """For every face used by a single cell: whether its node order must be
        reversed to point out of the domain."""

def build_cells(points, face_ptr, face_nodes, cell_ptr, cell_faces, positive):
    """Cells of an NFACE_n section.

    face_ptr/face_nodes: CSR of all NGON_n faces (0-based nodes); cell_ptr/
    cell_faces: CSR of the faces (0-based face indices) of each cell, positive:
    whether NFACE_n gives each of them a positive sign.

    Returns ``(blocks, boundary, reverse)``: blocks is a list of
    ``(cell_type, data, cell indices)``; boundary marks the faces used by one
    cell, and reverse whether their node order must be flipped to point out of
    the domain.
    """
