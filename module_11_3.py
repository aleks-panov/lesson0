import inspect
from pprint import pprint


def introspection_info(obj):
    type1 = type(obj)
    attribute1 = getattr(obj, '__dict__', None)
    methods1 = dir(obj)
    module1 = inspect.getmodule(obj)
    info = 'type:', type1, 'attributes:', attribute1, 'methods:', methods1, 'module:', module1
    return info


number_info = introspection_info(42)
pprint(number_info)
