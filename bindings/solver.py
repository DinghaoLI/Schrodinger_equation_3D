# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""Ceci est un module Python encapsule par SWIG"""


from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_solver', [dirname(__file__)])
        except ImportError:
            import _solver
            return _solver
        if fp is not None:
            try:
                _mod = imp.load_module('_solver', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _solver = swig_import_helper()
    del swig_import_helper
else:
    import _solver
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _solver.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _solver.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _solver.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _solver.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _solver.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _solver.SwigPyIterator_equal(self, x)

    def copy(self):
        return _solver.SwigPyIterator_copy(self)

    def next(self):
        return _solver.SwigPyIterator_next(self)

    def __next__(self):
        return _solver.SwigPyIterator___next__(self)

    def previous(self):
        return _solver.SwigPyIterator_previous(self)

    def advance(self, n):
        return _solver.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _solver.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _solver.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _solver.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _solver.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _solver.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _solver.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _solver.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class map_string_int(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_string_int, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_string_int, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _solver.map_string_int_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _solver.map_string_int___nonzero__(self)

    def __bool__(self):
        return _solver.map_string_int___bool__(self)

    def __len__(self):
        return _solver.map_string_int___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _solver.map_string_int___getitem__(self, key)

    def __delitem__(self, key):
        return _solver.map_string_int___delitem__(self, key)

    def has_key(self, key):
        return _solver.map_string_int_has_key(self, key)

    def keys(self):
        return _solver.map_string_int_keys(self)

    def values(self):
        return _solver.map_string_int_values(self)

    def items(self):
        return _solver.map_string_int_items(self)

    def __contains__(self, key):
        return _solver.map_string_int___contains__(self, key)

    def key_iterator(self):
        return _solver.map_string_int_key_iterator(self)

    def value_iterator(self):
        return _solver.map_string_int_value_iterator(self)

    def __setitem__(self, *args):
        return _solver.map_string_int___setitem__(self, *args)

    def asdict(self):
        return _solver.map_string_int_asdict(self)

    def __init__(self, *args):
        this = _solver.new_map_string_int(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def empty(self):
        return _solver.map_string_int_empty(self)

    def size(self):
        return _solver.map_string_int_size(self)

    def swap(self, v):
        return _solver.map_string_int_swap(self, v)

    def begin(self):
        return _solver.map_string_int_begin(self)

    def end(self):
        return _solver.map_string_int_end(self)

    def rbegin(self):
        return _solver.map_string_int_rbegin(self)

    def rend(self):
        return _solver.map_string_int_rend(self)

    def clear(self):
        return _solver.map_string_int_clear(self)

    def get_allocator(self):
        return _solver.map_string_int_get_allocator(self)

    def count(self, x):
        return _solver.map_string_int_count(self, x)

    def erase(self, *args):
        return _solver.map_string_int_erase(self, *args)

    def find(self, x):
        return _solver.map_string_int_find(self, x)

    def lower_bound(self, x):
        return _solver.map_string_int_lower_bound(self, x)

    def upper_bound(self, x):
        return _solver.map_string_int_upper_bound(self, x)
    __swig_destroy__ = _solver.delete_map_string_int
    __del__ = lambda self: None
map_string_int_swigregister = _solver.map_string_int_swigregister
map_string_int_swigregister(map_string_int)

class map_string_double(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_string_double, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_string_double, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _solver.map_string_double_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _solver.map_string_double___nonzero__(self)

    def __bool__(self):
        return _solver.map_string_double___bool__(self)

    def __len__(self):
        return _solver.map_string_double___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _solver.map_string_double___getitem__(self, key)

    def __delitem__(self, key):
        return _solver.map_string_double___delitem__(self, key)

    def has_key(self, key):
        return _solver.map_string_double_has_key(self, key)

    def keys(self):
        return _solver.map_string_double_keys(self)

    def values(self):
        return _solver.map_string_double_values(self)

    def items(self):
        return _solver.map_string_double_items(self)

    def __contains__(self, key):
        return _solver.map_string_double___contains__(self, key)

    def key_iterator(self):
        return _solver.map_string_double_key_iterator(self)

    def value_iterator(self):
        return _solver.map_string_double_value_iterator(self)

    def __setitem__(self, *args):
        return _solver.map_string_double___setitem__(self, *args)

    def asdict(self):
        return _solver.map_string_double_asdict(self)

    def __init__(self, *args):
        this = _solver.new_map_string_double(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def empty(self):
        return _solver.map_string_double_empty(self)

    def size(self):
        return _solver.map_string_double_size(self)

    def swap(self, v):
        return _solver.map_string_double_swap(self, v)

    def begin(self):
        return _solver.map_string_double_begin(self)

    def end(self):
        return _solver.map_string_double_end(self)

    def rbegin(self):
        return _solver.map_string_double_rbegin(self)

    def rend(self):
        return _solver.map_string_double_rend(self)

    def clear(self):
        return _solver.map_string_double_clear(self)

    def get_allocator(self):
        return _solver.map_string_double_get_allocator(self)

    def count(self, x):
        return _solver.map_string_double_count(self, x)

    def erase(self, *args):
        return _solver.map_string_double_erase(self, *args)

    def find(self, x):
        return _solver.map_string_double_find(self, x)

    def lower_bound(self, x):
        return _solver.map_string_double_lower_bound(self, x)

    def upper_bound(self, x):
        return _solver.map_string_double_upper_bound(self, x)
    __swig_destroy__ = _solver.delete_map_string_double
    __del__ = lambda self: None
map_string_double_swigregister = _solver.map_string_double_swigregister
map_string_double_swigregister(map_string_double)

class map_string_string(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, map_string_string, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, map_string_string, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _solver.map_string_string_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _solver.map_string_string___nonzero__(self)

    def __bool__(self):
        return _solver.map_string_string___bool__(self)

    def __len__(self):
        return _solver.map_string_string___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _solver.map_string_string___getitem__(self, key)

    def __delitem__(self, key):
        return _solver.map_string_string___delitem__(self, key)

    def has_key(self, key):
        return _solver.map_string_string_has_key(self, key)

    def keys(self):
        return _solver.map_string_string_keys(self)

    def values(self):
        return _solver.map_string_string_values(self)

    def items(self):
        return _solver.map_string_string_items(self)

    def __contains__(self, key):
        return _solver.map_string_string___contains__(self, key)

    def key_iterator(self):
        return _solver.map_string_string_key_iterator(self)

    def value_iterator(self):
        return _solver.map_string_string_value_iterator(self)

    def __setitem__(self, *args):
        return _solver.map_string_string___setitem__(self, *args)

    def asdict(self):
        return _solver.map_string_string_asdict(self)

    def __init__(self, *args):
        this = _solver.new_map_string_string(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def empty(self):
        return _solver.map_string_string_empty(self)

    def size(self):
        return _solver.map_string_string_size(self)

    def swap(self, v):
        return _solver.map_string_string_swap(self, v)

    def begin(self):
        return _solver.map_string_string_begin(self)

    def end(self):
        return _solver.map_string_string_end(self)

    def rbegin(self):
        return _solver.map_string_string_rbegin(self)

    def rend(self):
        return _solver.map_string_string_rend(self)

    def clear(self):
        return _solver.map_string_string_clear(self)

    def get_allocator(self):
        return _solver.map_string_string_get_allocator(self)

    def count(self, x):
        return _solver.map_string_string_count(self, x)

    def erase(self, *args):
        return _solver.map_string_string_erase(self, *args)

    def find(self, x):
        return _solver.map_string_string_find(self, x)

    def lower_bound(self, x):
        return _solver.map_string_string_lower_bound(self, x)

    def upper_bound(self, x):
        return _solver.map_string_string_upper_bound(self, x)
    __swig_destroy__ = _solver.delete_map_string_string
    __del__ = lambda self: None
map_string_string_swigregister = _solver.map_string_string_swigregister
map_string_string_swigregister(map_string_string)

class Solver(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solver, name)
    __repr__ = _swig_repr
    __swig_setmethods__["psi"] = _solver.Solver_psi_set
    __swig_getmethods__["psi"] = _solver.Solver_psi_get
    if _newclass:
        psi = _swig_property(_solver.Solver_psi_get, _solver.Solver_psi_set)

    def __init__(self, *args):
        this = _solver.new_Solver(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def ftcs(self):
        return _solver.Solver_ftcs(self)

    def btcs(self, arg2):
        return _solver.Solver_btcs(self, arg2)

    def ctcs(self, arg2):
        return _solver.Solver_ctcs(self, arg2)
    __swig_destroy__ = _solver.delete_Solver
    __del__ = lambda self: None
Solver_swigregister = _solver.Solver_swigregister
Solver_swigregister(Solver)

# This file is compatible with both classic and new-style classes.

