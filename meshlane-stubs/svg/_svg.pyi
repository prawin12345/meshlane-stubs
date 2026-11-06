from .._exceptions import WriteError as WriteError
from .._helpers import register_format as register_format

def write(filename, mesh, float_fmt: str = '.3f', stroke_width: str | None = None, image_width: int | float | None = 100, fill: str = '#c8c5bd', stroke: str = '#000080'): ...
