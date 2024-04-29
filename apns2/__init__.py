try:
    from collections import Iterable, Mapping, MutableSet, MutableMapping
except ImportError:
    import collections
    collections.Iterable = collections.abc.Iterable
    collections.Mapping = collections.abc.Mapping
    collections.MutableSet = collections.abc.MutableSet
    collections.MutableMapping = collections.abc.MutableMapping

