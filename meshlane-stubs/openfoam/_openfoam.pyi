import numpy as np
from .._common import warn as warn
from .._exceptions import WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

logger: Incomplete

class _RaggedArray:
    """
    Rows of variable length stored in CSR (compressed sparse row) form.

    A polyMesh has two ragged integer relations -- faces (node ids per face)
    and cell topology (face ids per cell) -- both of which would cost several
    gigabytes as a Python ``list[list[int]]`` on an industrial mesh (tens of
    millions of rows). CSR stores them as two flat numpy arrays instead:

    * ``conn`` -- every row's values concatenated back to back;
    * ``off``  -- length ``n_rows + 1``, so row ``i`` is
      ``conn[off[i]:off[i + 1]]``.

    Indexing (``a[i]``) and ``len(a)`` behave like the list-of-lists they
    replace, so consumers need no special-casing.
    """
    conn: Incomplete
    off: Incomplete
    def __init__(self, conn: np.ndarray, off: np.ndarray) -> None: ...
    @classmethod
    def from_lists(cls, rows: list) -> _RaggedArray:
        """Build from a Python list-of-lists (used for small ASCII inputs)."""
    def __len__(self) -> int: ...
    def __getitem__(self, i: int) -> np.ndarray: ...
    def sizes(self) -> np.ndarray:
        """Length of every row, as a numpy array."""
    def to_lists(self) -> list:
        """Materialise back to a Python list-of-lists (used by tests)."""

def read(filename) -> Mesh:
    """Read an OpenFOAM polyMesh case and return a :class:`meshlane.Mesh`."""
def write(filename, mesh, binary: bool = False, float_fmt: str = '.17g', **kwargs) -> None:
    """Write a :class:`meshlane.Mesh` as an OpenFOAM polyMesh.

    With ``binary=True``, points, faces, owner and neighbour are written in
    OpenFOAM's binary format (little endian, 32-bit labels, 64-bit scalars;
    faces as a ``faceCompactList``), which is smaller and much faster to write
    and read. ``boundary`` stays ASCII, as OpenFOAM writes it.

    ``filename`` is a ``.foam`` file (the polyMesh goes to
    ``<its directory>/constant/polyMesh`` and the empty ``.foam`` file is
    created), a case directory, or a ``polyMesh`` directory.
    """
