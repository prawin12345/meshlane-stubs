from ._common import num_nodes_per_cell as num_nodes_per_cell, warn as warn
from ._exceptions import ReadError as ReadError
from ._mesh import CellBlock as CellBlock
from _typeshed import Incomplete

vtk_to_meshio_type: Incomplete
meshio_to_vtk_type: Incomplete

def vtk_to_meshio_order(vtk_type, dtype=...): ...
def meshio_to_vtk_order(meshio_type, dtype=...): ...
def vtk_cells_from_data(connectivity, offsets, types, cell_data_raw): ...

class Info:
    """Info Container for the VTK reader."""
    points: Incomplete
    field_data: Incomplete
    cell_data_raw: Incomplete
    point_data: Incomplete
    dataset: Incomplete
    connectivity: Incomplete
    offsets: Incomplete
    types: Incomplete
    active: Incomplete
    is_ascii: bool
    split: Incomplete
    num_items: int
    section: Incomplete
    def __init__(self) -> None: ...
