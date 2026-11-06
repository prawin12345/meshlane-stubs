from _typeshed import Incomplete

ORIENTABLE_TYPES: Incomplete

def consistent_orientation_flips(blocks, points):
    '''Compute per-block boolean flip masks that make 3D-cell orientation
    globally consistent for MED.

    blocks: list of dicts, in the order cells are laid out, each either
        {"kind": "regular", "type": <med cell type>, "conn": (n,k) int array}
        {"kind": "polyhedron", "faces": [ [face_node_array, ...], ... ]}
      All node ids are 0-based, in the final MED node ordering.
    points: (n_points, 3) float array.

    Returns a list (aligned with blocks) of boolean masks (True = flip that
    cell), or None if there is nothing to do or the mesh is already consistent.
    '''
def apply_regular_flip(cell_type, conn, mask):
    """Return conn with flipped rows reversed by the type's node permutation."""
def apply_polyhedron_flip(faces_list, mask):
    """Return polyhedra with each flipped cell's faces reversed (winding
    flipped) so its outward normals invert consistently."""
