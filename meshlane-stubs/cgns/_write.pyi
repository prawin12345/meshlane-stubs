from .._common import warn as warn
from .._exceptions import WriteError as WriteError
from _typeshed import Incomplete

VERSION: float

class _Writer:
    f: Incomplete
    compression: Incomplete
    compression_opts: Incomplete
    def __init__(self, f, compression, compression_opts) -> None: ...
    def node(self, parent, name, label, value=None):
        """A CGNS node; value is a numpy array (2D arrays given in SIDS order,
        stored transposed as CGNS arrays are Fortran ordered), a string (C1) or
        None (MT)."""

class _Names:
    """CGNS node names: at most 32 characters, no '/', unique among siblings."""
    used: Incomplete
    renamed: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, name): ...

def write(filename, mesh, compression=None, compression_opts=None) -> None: ...
def write_multi(filename, meshes, mesh_names=None, compression=None, compression_opts=None) -> None:
    """Write several meshes to one CGNS file: one base, one zone per mesh. The
    groups of all zones share the families of the base."""

class _Families:
    """Family_t names of a base, shared by its zones."""
    names: Incomplete
    names_: Incomplete
    def __init__(self) -> None: ...
    def __call__(self, group): ...

class _Layout:
    """Element sections of a mesh, and the CGNS element number of every cell."""
    blocks: Incomplete
    cell_sets: Incomplete
    cell_dim: Incomplete
    sections: Incomplete
    numbers: Incomplete
    next: int
    num_cells: int
    def __init__(self, blocks, cell_sets, cell_dim) -> None: ...
    def add(self, name, code, conn, count, block=None, local=None, **extra): ...
    def boundary_groups(self):
        """[(group, (dim, element numbers))] of the cell sets on lower
        dimensional blocks, one entry per group and dimension."""
    def volume_values(self, per_block):
        """Values of a cell data field on the volume cells, in element order, or
        None when the field does not cover them."""
