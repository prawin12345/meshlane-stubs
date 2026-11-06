def label(node): ...
def name(node): ...
def data(node):
    """Value of a node as a numpy array, or None."""
def text(node):
    """Value of a character (C1) node."""
def resolve(node):
    '''Target of a CGNS link node (data type ``LK``), or the node itself.

    A link node holds the target file and path, and an HDF5 link ``" link"`` to
    it; when HDF5 cannot follow that one, the file is looked up next to the file
    holding the link.'''
def children(node, node_label):
    """Child nodes with the given label (links resolved), in the file's order."""
def child(node, node_label):
    """First child node with the given label, or None."""
def file_version(f):
    """CGNS version that wrote the file, as an integer (3.1 -> 3100)."""
