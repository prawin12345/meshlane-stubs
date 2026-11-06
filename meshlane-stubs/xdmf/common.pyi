import numpy as np
from .._exceptions import ReadError as ReadError
from .._mesh import CellBlock as CellBlock
from numpy.typing import NDArray as NDArray

numpy_to_xdmf_dtype: dict[str, tuple[str, str]]
xdmf_to_numpy_type: dict[tuple[str, str], str]
dtype_to_format_string: dict[str, str]
meshio_to_xdmf_type: dict[str, list[str]]
xdmf_to_meshio_type: dict[str, str]
xdmf_idx_to_meshio_type: dict[int, str]
meshio_type_to_xdmf_index: dict[str, int]

def translate_mixed_cells(data: NDArray[np.integer]) -> list[CellBlock]: ...
def attribute_type(data: np.ndarray) -> str: ...
