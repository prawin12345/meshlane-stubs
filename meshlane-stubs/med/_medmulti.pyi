from .._common import num_nodes_per_cell as num_nodes_per_cell
from .._exceptions import WriteError as WriteError
from .._mesh import Mesh as Mesh
from ._med import MED_FLOAT64 as MED_FLOAT64, med_geo_code as med_geo_code, med_to_geo_type as med_to_geo_type, med_type_to_entity as med_type_to_entity, meshio_to_med_type as meshio_to_med_type, numpy_to_med_type as numpy_to_med_type, numpy_void_str as numpy_void_str
from ._med41 import FieldBitmaskWriter as FieldBitmaskWriter

def write_med_multi(filename, meshes, mesh_names=None, med_version: str = '4.1.0', **kwargs) -> None:
    """Write several meshes to one MED file.

    Wraps the real writer so that HDF5 link-creation-order tracking is enabled
    for the whole file (required by medfile / Salome) and restored afterwards.
    """
def read_med_multi(filename, **kwargs):
    """Read a multi-mesh MED file. Returns (meshes, mesh_names)."""
