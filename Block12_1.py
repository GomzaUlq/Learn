import sys
from inspect import getmodule


def introspection_info(obj):
    x = obj + 3
    return x


number = introspection_info(42)
print(number)


def introspection(obj):
    return dict(Type=type(obj).__name__, Attribute=obj.__dict__, Method=dir(obj), Module=getmodule(obj))


info = introspection(introspection_info)
print(info)
