import numpy
from setuptools import setup, Extension

module1 = Extension('_solver',
                    include_dirs = ['./armanpy/'],
                    libraries = ['m', 'z', 'armadillo'],
                    sources = ['solver.i', '../src/Solver.cpp'],
                    swig_opts = ["-c++", "-Wall", "-I.", "-I./include/armanpy/"])

setup (name = 'package_test',
       py_modules = ['solver'],
       version = '1.0',
       description = 'This is a test package',
       ext_modules = [module1],
       include_dirs = [numpy.get_include()]
       )
