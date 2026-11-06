import numpy as np
from ._common import error as error, num_nodes_per_cell as num_nodes_per_cell
from ._exceptions import ReadError as ReadError, WriteError as WriteError
from ._files import is_buffer as is_buffer
from ._mesh import CellBlock as CellBlock, Mesh as Mesh
from collections.abc import Callable as Callable
from os import PathLike

extension_to_filetypes: dict[str, list[str]]
reader_map: dict[str, Callable[[str | PathLike[str]], Mesh]]

def register_format(format_name: str, extensions: list[str], reader: Callable[[str | PathLike[str]], Mesh], writer_map: dict[str, Callable[[str | PathLike[str], Mesh], None]]) -> None: ...
def deregister_format(format_name: str): ...
def read(filename: str | PathLike[str], file_format: str | None = None) -> Mesh:
    """Reads an unstructured mesh with added data.

    :param filenames: The files/PathLikes to read from.
    :type filenames: str

    :returns mesh{2,3}d: The mesh data.
    """
def write_points_cells(filename: str | PathLike[str], points: np.ndarray, cells: dict[str, np.ndarray] | list[tuple[str, np.ndarray] | CellBlock], point_data: dict[str, np.ndarray] | None = None, cell_data: dict[str, list[np.ndarray]] | None = None, field_data=None, point_sets: dict[str, np.ndarray] | None = None, cell_sets: dict[str, list[np.ndarray]] | None = None, file_format: str | None = None, **kwargs) -> None: ...
def write(filename: str | PathLike[str], mesh: Mesh, file_format: str | None = None) -> None:
    """Writes mesh together with data to a file.

    :params filename: File to write to.
    :type filename: str

    :params point_data: Named additional point data to write to the file.
    :type point_data: dict
    """
