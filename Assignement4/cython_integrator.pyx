#needs to be compiled via setup.py to make function importable/callable


import numpy
cimport numpy

cpdef double cython_integrate(f,double a,double b,int N): #interval e: [b, a]

	cdef double dx = (b-a)/float(N)
	cdef numpy.ndarray[numpy.double_t, ndim=1] x
	cdef numpy.ndarray[numpy.double_t, ndim=1] function
	cdef double integral
	#x = numpy.linspace(a,b,N)
	x = numpy.linspace((a+dx),(b+dx),N+1)
	#print(x)
	#print(f(x))
	try:
		#function = numpy.asarray(f(x)) #possibly a better way of handling function?
		function = numpy.asarray(f(x[:-1]))
		#print(function)
	
		integral = numpy.sum(function)*dx
	#if (numpy.size(function) == 1):
	except ValueError:
		integral = (f(x)*dx)*N # handles constant functions #slows down the function though
		#print(integral)
	#for i in range(1,N+1): # using trailing edge point
	#	integral += function[i]*dx
		
	return integral

cpdef double cython_midpoint_integrate(f,double a,double b,int N): #interval e: [b, a]

	cdef double dx = (b-a)/float(N)
	cdef numpy.ndarray[numpy.double_t, ndim=1] x
	cdef numpy.ndarray[numpy.double_t, ndim=1] function
	cdef double integral
	#x = numpy.linspace(a+(dx/2),b+(dx/2),N)
	x = numpy.linspace((a+(dx/2.)),(b+(dx/2.)),N+1)
	#print(x)
	#print(f(x))
	try:
		#function = numpy.asarray(f(x)) #possibly a better way of handling function?
		function = numpy.asarray(f(x[:-1]))
		#print(function)
	
		integral = numpy.sum(function)*dx
	#if (numpy.size(function) == 1):
	except ValueError:
		integral = (f(x)*dx)*N # handles constant functions #slows down the function though
		#print(integral)
	#for i in range(1,N+1): # using trailing edge point
	#	integral += function[i]*dx
		
	return integral

