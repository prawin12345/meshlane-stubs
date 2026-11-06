from ._tree import child as child, children as children, data as data, name as name, resolve as resolve, text as text

def location(node, version):
    '''GridLocation of a BC or FlowSolution node ("Vertex" by default).'''
def family_names(node, version):
    """Families of a node (FamilyName_t, then AdditionalFamilyName_t)."""
def boundary_conditions(zone, version):
    '''``[(name, kind, values)]`` for the BCs of a zone, kind being "elements"
    (1-based element numbers) or "points" (1-based node numbers).'''
def subregions(zone, version):
    '''``[(name, kind, values)]`` for the ZoneSubRegion_t nodes of a zone that list
    nodes ("region points": point sets only) or elements.'''
