import numpy as np
from ._common import num_nodes_per_cell as num_nodes_per_cell, warn as warn
from _typeshed import Incomplete
from numpy.typing import NDArray as NDArray
from os import PathLike
from typing import Mapping, Self, Sequence

topological_dimension: dict[str, int]

class CellBlock:
    type: str
    data: NDArray[np.integer]
    dim: int
    tags: list[str]
    def __init__(self, cell_type: str, data: np.ndarray, tags: list[str] | None = None) -> None: ...
    def __len__(self) -> int: ...

class Mesh:
    points: NDArray[np.floating]
    cells: list[CellBlock]
    cell_sets: dict[str, list[NDArray[np.integer]]]
    field_data: Mapping[str, NDArray[np.integer] | list[int]]
    point_data: dict[str, NDArray[np.floating]]
    point_sets: dict[str, NDArray[np.integer]]
    cell_data: dict[str, list[NDArray[np.floating]]]
    gmsh_periodic: Incomplete
    info: Incomplete
    def __init__(self, points: NDArray[np.floating] | list[list[float]], cells: dict[str, np.ndarray] | Sequence[tuple[str, np.ndarray] | CellBlock], point_data: dict[str, np.ndarray] | None = None, cell_data: dict[str, list[NDArray[np.floating]]] | None = None, field_data: Mapping[str, NDArray[np.integer] | list[int]] | None = None, point_sets: dict[str, NDArray[np.integer]] | None = None, cell_sets: dict[str, list[NDArray[np.integer]]] | None = None, gmsh_periodic=None, info=None) -> None: ...
    def copy(self) -> Self: ...
    def write(self, path_or_buf: str | PathLike[str], file_format: str | None = None, **kwargs) -> None: ...
    def get_cells_type(self, cell_type: str) -> NDArray[np.integer]: ...
    def get_cell_data(self, name: str, cell_type: str) -> NDArray[np.floating]: ...
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
    def cells_dict(self) -> dict[str, NDArray[np.integer]]: ...
    @property
    def cell_data_dict(self) -> dict[str, dict[str, NDArray[np.floating]]]: ...
    @property
    def cell_sets_dict(self) -> dict[str, dict[str, NDArray[np.integer]]]: ...
    @classmethod
    def read(cls, path_or_buf: str | PathLike[str], file_format: str | None = None) -> Mesh: ...
    def cell_sets_to_data(self, data_name: str | None = None) -> None: ...
    def point_sets_to_data(self, join_char: str = '-') -> None: ...
    def cell_data_to_sets(self, key: str) -> None:
        """Convert point_data to cell_sets."""
    def point_data_to_sets(self, key: str) -> None:
        """Convert point_data to point_sets."""
