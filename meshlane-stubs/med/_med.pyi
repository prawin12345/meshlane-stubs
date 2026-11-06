from .._common import num_nodes_per_cell as num_nodes_per_cell
from .._exceptions import ReadError as ReadError, WriteError as WriteError
from .._helpers import register_format as register_format
from .._mesh import Mesh as Mesh
from ._med41 import FieldBitmaskWriter as FieldBitmaskWriter
from _typeshed import Incomplete

meshio_to_med_type: Incomplete
med_to_meshio_type: Incomplete
numpy_void_str: Incomplete
MED_FLOAT32: int
MED_FLOAT64: int
MED_INT32: int
MED_INT64: int
numpy_to_med_type: Incomplete
med_to_geo_type: Incomplete
med_type_to_entity: Incomplete
med_geo_code: Incomplete

def read(filename): ...
def write(filename, mesh, med_version: str = '4.1.0', **kwargs): ...
