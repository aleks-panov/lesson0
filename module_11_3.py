import inspect


def introspection_info(obj):
    type1 = type(obj)
    attribute1 = getattr(obj, '__dict__', None)
    methods1 = [method for method in dir(obj) if callable(getattr(obj, method))]
    module1 = (inspect.getmodule(obj))
    info = 'type:', type1, 'attributes:', attribute1, 'methods:', methods1, 'module:', module1
    return info


number_info = introspection_info(42)
print(number_info)
