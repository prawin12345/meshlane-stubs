from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._files import open_file as open_file
from .._helpers import register_format as register_format
from .._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete

float_pattern: str
float_re: Incomplete
point_pattern: Incomplete
point_re: Incomplete
triangle_pattern: Incomplete
triangle_re: Incomplete
tin_pattern: Incomplete
tin_re: Incomplete

def read_str(s): ...
def arr_to_str(arr): ...
def read(filename): ...
def write(filename, mesh) -> None: ...
def write_buffer(f, mesh) -> None: ...
def write_str(mesh): ...
