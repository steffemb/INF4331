Module for numerical integration. Each method has one edge point scheme, and
one centered scheme. The centered scheme converges fastest in most cases


CONVENTION:
place package folder in directory of python script.

import as 

from package.integrator import <function name>

Each function is then callable as integrate(f,a,b,N)

to integrate f from a to b with N as resolution.

"f" must be a lambda (or callable python should work?) function ex: "f = lambda x: x*x"
for x^2.


SETUP:

Run command "python setup.py build_ext --inplace" in directory


NOTE:

numba integrator is porly implemented and not recomended for use at this point

numpy integrator is fastest for "small" N. and cython is fastest for "large" N.
