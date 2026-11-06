from .._common import warn as warn
from ._groups import location as location
from ._tree import child as child, children as children, data as data, name as name, resolve as resolve

def zone_fields(zone, version):
    """``[(field name, location, values)]`` of the numeric arrays of the
    FlowSolution nodes of a zone. A field name found in several solutions gets the
    solution name as suffix."""
