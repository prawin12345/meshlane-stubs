from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager

def is_buffer(obj, mode): ...
@contextmanager
def open_file(path_or_buf, mode: str = 'r') -> Generator[Incomplete]: ...
