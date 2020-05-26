# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_PcbPlacer')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_PcbPlacer')
    _PcbPlacer = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_PcbPlacer', [dirname(__file__)])
        except ImportError:
            import _PcbPlacer
            return _PcbPlacer
        try:
            _mod = imp.load_module('_PcbPlacer', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _PcbPlacer = swig_import_helper()
    del swig_import_helper
else:
    import _PcbPlacer
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class GridBasedPlacer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GridBasedPlacer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GridBasedPlacer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["iii"] = _PcbPlacer.GridBasedPlacer_iii_set
    __swig_getmethods__["iii"] = _PcbPlacer.GridBasedPlacer_iii_get
    if _newclass:
        iii = _swig_property(_PcbPlacer.GridBasedPlacer_iii_get, _PcbPlacer.GridBasedPlacer_iii_set)

    def __init__(self, db: 'kicadPcbDataBase &'):
        this = _PcbPlacer.new_GridBasedPlacer(db)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _PcbPlacer.delete_GridBasedPlacer
    __del__ = lambda self: None

    def test_hplacer_flow(self) -> "void":
        return _PcbPlacer.GridBasedPlacer_test_hplacer_flow(self)

    def test_placer_flow(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_test_placer_flow(self)

    def getDb(self) -> "kicadPcbDataBase &":
        return _PcbPlacer.GridBasedPlacer_getDb(self)
    __swig_setmethods__["mDb"] = _PcbPlacer.GridBasedPlacer_mDb_set
    __swig_getmethods__["mDb"] = _PcbPlacer.GridBasedPlacer_mDb_get
    if _newclass:
        mDb = _swig_property(_PcbPlacer.GridBasedPlacer_mDb_get, _PcbPlacer.GridBasedPlacer_mDb_set)

    def get_total_cost(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_get_total_cost(self)

    def get_wirelength_cost(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_get_wirelength_cost(self)

    def get_overlap_cost(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_get_overlap_cost(self)

    def get_temperature(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_get_temperature(self)

    def set_base_lam(self, _lam: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_base_lam(self, _lam)

    def set_wirelength_weight(self, _cst: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_wirelength_weight(self, _cst)

    def set_lambda_schedule(self, _lsched: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_lambda_schedule(self, _lsched)

    def set_two_sided(self, _2sided: 'bool') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_two_sided(self, _2sided)

    def set_initial_move_radius(self, _eps: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_initial_move_radius(self, _eps)

    def set_rtree(self, _rt: 'bool') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_rtree(self, _rt)

    def set_lam(self, _lam: 'bool') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_lam(self, _lam)

    def set_lamtemp_update(self, _coef: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_lamtemp_update(self, _coef)

    def set_num_iterations(self, iter: 'int') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_num_iterations(self, iter)

    def set_iterations_moves(self, iter: 'int') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_iterations_moves(self, iter)

    def set_initial_temperature(self, tmp: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_set_initial_temperature(self, tmp)

    def h_cellDensity(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_h_cellDensity(self)

    def h_initialize_params(self, netToCell: 'map< int,vector< Module * > > &') -> "void":
        return _PcbPlacer.GridBasedPlacer_h_initialize_params(self, netToCell)

    def h_validate_move(self, node: 'Module *', rx: 'double', ry: 'double') -> "void":
        return _PcbPlacer.GridBasedPlacer_h_validate_move(self, node, rx, ry)

    def h_cost(self, netToCell: 'map< int,vector< Module * > > &', temp_debug: 'int'=0) -> "double":
        return _PcbPlacer.GridBasedPlacer_h_cost(self, netToCell, temp_debug)

    def h_cost_partial(self, nodes: 'vector< Module * > &', netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_cost_partial(self, nodes, netToCell)

    def h_cell_overlap(self) -> "double":
        return _PcbPlacer.GridBasedPlacer_h_cell_overlap(self)

    def h_wirelength(self, netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_wirelength(self, netToCell)

    def h_cell_overlap_partial(self, nodes: 'vector< Module * > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_cell_overlap_partial(self, nodes)

    def h_wirelength_partial(self, nodes: 'vector< Module * > &', netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_wirelength_partial(self, nodes, netToCell)

    def h_rudy(self, netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_rudy(self, netToCell)

    def h_annealer(self, netToCell: 'map< int,vector< Module * > > &', initial_pl: 'string', level: 'int'=0) -> "float":
        return _PcbPlacer.GridBasedPlacer_h_annealer(self, netToCell, initial_pl, level)

    def h_initialize_temperature(self, Temperature: 'double &', netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_initialize_temperature(self, Temperature, netToCell)

    def h_initiate_move(self, current_cost: 'double', netToCell: 'map< int,vector< Module * > > &') -> "double":
        return _PcbPlacer.GridBasedPlacer_h_initiate_move(self, current_cost, netToCell)

    def h_random_placement(self, xmin: 'int', xmax: 'int', ymin: 'int', ymax: 'int', n: 'Module &') -> "void":
        return _PcbPlacer.GridBasedPlacer_h_random_placement(self, xmin, xmax, ymin, ymax, n)

    def h_random_initial_placement(self) -> "void":
        return _PcbPlacer.GridBasedPlacer_h_random_initial_placement(self)

    def h_check_move(self, prevCost: 'double', newCost: 'double', Temperature: 'double &') -> "bool":
        return _PcbPlacer.GridBasedPlacer_h_check_move(self, prevCost, newCost, Temperature)

    def h_random_node(self) -> "vector< Module * >::iterator":
        return _PcbPlacer.GridBasedPlacer_h_random_node(self)
GridBasedPlacer_swigregister = _PcbPlacer.GridBasedPlacer_swigregister
GridBasedPlacer_swigregister(GridBasedPlacer)

# This file is compatible with both classic and new-style classes.


