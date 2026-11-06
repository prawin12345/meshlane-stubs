from .. import su2 as su2
from ..med import read_med_multi as read_med_multi, write_med_multi as write_med_multi

def multi_format(path, file_format=None):
    '''The multi-mesh format of ``path`` ("med", "su2"), or None.'''
def read_multi(path, file_format=None):
    """``(meshes, names)`` of a MED or SU2 file."""
def write_multi(path, meshes, mesh_names=None, file_format=None) -> None: ...
