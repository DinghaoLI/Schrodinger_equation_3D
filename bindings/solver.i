%module (docstring="Ceci est un module Python encapsule par SWIG") solver
%include "stl.i"
%include "std_map.i"
%include "std_string.i"
%include "std_vector.i"
%include "std_vectora.i"
%include "exception.i"

namespace std
{
  %template(map_string_int) map<string, int>;
  %template(map_string_double) map<string, double>;
  %template(map_string_string) map<string, string>;
}

%{
#define SWIG_FILE_WITH_INIT
#include "../src/Solver.h"
%}
%include "numpy.i"
%include "armanpy.i"
%include "../src/Solver.h"