import numpy as np
from ._common import num_nodes_per_cell as num_nodes_per_cell, warn as warn
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

topological_dimension: Incomplete

class CellBlock:
    type: Incomplete
    data: Incomplete
    dim: int
    tags: Incomplete
    def __init__(self, cell_type: str, data: list | np.ndarray, tags: list[str] | None = None) -> None: ...
    def __len__(self) -> int: ...

class Mesh:
    points: Incomplete
    cells: Incomplete
    point_data: Incomplete
    cell_data: Incomplete
    field_data: Incomplete
    point_sets: Incomplete
    cell_sets: Incomplete
    gmsh_periodic: Incomplete
    info: Incomplete
    def __init__(self, points: ArrayLike, cells: dict[str, ArrayLike] | list[tuple[str, ArrayLike] | CellBlock], point_data: dict[str, ArrayLike] | None = None, cell_data: dict[str, list[ArrayLike]] | None = None, field_data=None, point_sets: dict[str, ArrayLike] | None = None, cell_sets: dict[str, list[ArrayLike]] | None = None, gmsh_periodic=None, info=None) -> None: ...
    def copy(self): ...
    def write(self, path_or_buf, file_format: str | None = None, **kwargs): ...
    def get_cells_type(self, cell_type: str): ...
    def get_cell_data(self, name: str, cell_type: str): ...
    def remove_duplicate_cells(self, dry_run: bool = False):
        '''Remove cells that duplicate another cell of the same type (identical
        node set, order-independent), keeping the first occurrence. Returns the
        number removed; with ``dry_run=True`` returns the number that *would* be
        removed without modifying the mesh.

        ``cell_data`` and ``cell_sets`` are remapped onto the surviving cells.
        Only fixed-shape ("regular") cell types are considered; ``polyhedron``
        and ``polygon`` blocks (whose rows are not flat node lists) are left
        untouched.

        Coincident cells occupy the same space and can cause connectivity errors
        in downstream solvers (e.g. code_saturne). This is opt-in: meshlane keeps
        the mesh faithful by default.
        '''
    @property
    def cells_dict(self): ...
    @property
    def cell_data_dict(self): ...
    @property
    def cell_sets_dict(self): ...
    @classmethod
    def read(cls, path_or_buf, file_format=None): ...
    def cell_sets_to_data(self, data_name: str | None = None): ...
    def point_sets_to_data(self, join_char: str = '-') -> None: ...
    def cell_data_to_sets(self, key: str):
        """Convert point_data to cell_sets."""
    def point_data_to_sets(self, key: str):
        """Convert point_data to point_sets."""
