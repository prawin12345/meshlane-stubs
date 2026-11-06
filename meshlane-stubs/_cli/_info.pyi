from .._common import warn as warn
from .._exceptions import ReadError as ReadError
from .._helpers import read as read, reader_map as reader_map
from ._multi import multi_format as multi_format, read_multi as read_multi

def add_args(parser) -> None: ...
def info(args): ...
