from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from typing import IO
from typing_extensions import TypeIs

def is_buffer(obj: object, mode: str) -> TypeIs[IO]: ...
@contextmanager
def open_file(path_or_buf, mode: str = 'r') -> Generator[Incomplete]: ...
