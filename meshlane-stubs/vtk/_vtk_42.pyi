from ..__about__ import __version__ as __version__
from .._common import warn as warn
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._files import open_file as open_file
from .._mesh import Mesh as Mesh
from .._vtk_common import Info as Info, meshio_to_vtk_order as meshio_to_vtk_order, meshio_to_vtk_type as meshio_to_vtk_type, vtk_to_meshio_order as vtk_to_meshio_order, vtk_to_meshio_type as vtk_to_meshio_type
from _typeshed import Incomplete

vtk_type_to_numnodes: Incomplete
vtk_to_numpy_dtype_name: Incomplete
numpy_to_vtk_dtype: Incomplete
vtk_dataset_types: Incomplete
vtk_dataset_infos: Incomplete
vtk_sections: Incomplete

def read(filename): ...
def read_buffer(f): ...
def translate_cells(connectivity, types, cell_data_raw): ...
def write(filename, mesh, binary: bool = True): ...
