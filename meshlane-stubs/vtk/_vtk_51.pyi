from ..__about__ import __version__ as __version__
from .._common import info as info, join_strings as join_strings, replace_space as replace_space, warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._mesh import Mesh as Mesh
from .._vtk_common import Info as Info, meshio_to_vtk_order as meshio_to_vtk_order, meshio_to_vtk_type as meshio_to_vtk_type, vtk_cells_from_data as vtk_cells_from_data
from _typeshed import Incomplete

vtk_to_numpy_dtype_name: Incomplete
numpy_to_vtk_dtype: Incomplete
vtk_dataset_types: Incomplete
vtk_dataset_infos: Incomplete
vtk_sections: Incomplete

def read(filename): ...
def read_buffer(f): ...
def write(filename, mesh, binary: bool = True) -> None: ...
