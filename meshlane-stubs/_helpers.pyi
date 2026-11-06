from ._common import error as error, num_nodes_per_cell as num_nodes_per_cell
from ._exceptions import ReadError as ReadError, WriteError as WriteError
from ._files import is_buffer as is_buffer
from ._mesh import CellBlock as CellBlock, Mesh as Mesh
from _typeshed import Incomplete
from numpy.typing import ArrayLike as ArrayLike

extension_to_filetypes: Incomplete
reader_map: Incomplete

def register_format(format_name: str, extensions: list[str], reader, writer_map) -> None: ...
def deregister_format(format_name: str): ...
def read(filename, file_format: str | None = None):
    """Reads an unstructured mesh with added data.

    :param filenames: The files/PathLikes to read from.
    :type filenames: str

    :returns mesh{2,3}d: The mesh data.
    """
def write_points_cells(filename, points: ArrayLike, cells: dict[str, ArrayLike] | list[tuple[str, ArrayLike] | CellBlock], point_data: dict[str, ArrayLike] | None = None, cell_data: dict[str, list[ArrayLike]] | None = None, field_data=None, point_sets: dict[str, ArrayLike] | None = None, cell_sets: dict[str, list[ArrayLike]] | None = None, file_format: str | None = None, **kwargs): ...
def write(filename, mesh: Mesh, file_format: str | None = None, **kwargs):
    """Writes mesh together with data to a file.

    :params filename: File to write to.
    :type filename: str

    :params point_data: Named additional point data to write to the file.
    :type point_data: dict
    """
