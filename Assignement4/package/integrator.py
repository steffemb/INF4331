
import numpy as np
from cython_integrator import cython_integrate
from cython_integrator import cython_midpoint_integrate

from numba import jit

def integrate(f,a,b,N): #interval e: [b, a]
	#print("integrating %s"%str(inspect.getsourcelines(f)[0][0]))
	dx = (b-a)/float(N)	
	integral = 0
	for i in range(1,N): # using trailing edge point
		integral += f(i*dx)*dx
		
	return integral

def midpoint_integrate(f,a,b,N): #interval e: [b, a]
	#print("integrating %s"%str(inspect.getsourcelines(f)[0][0]))
	dx = (b-a)/float(N)	
	integral = 0
	for i in range(0,N): # using midpoint point
		integral += f(i*dx + (dx/2.))*dx
		#print(i*dx - (dx/2))
		
	return integral


def numpy_integrate(f,a,b,N): #interval e: [b, a]

	dx = (b-a)/float(N)
	x = np.linspace((a+dx),(b+dx),N+1) # uses leading point?
	
	function = np.asarray(f(x[:-1]))
	#print(function)
	integral = np.sum(function)*dx
	if (np.size(function) == 1):
		integral = integral*N # handles constant functions
	#for i in range(1,N+1): # using trailing edge point
	#	integral += function[i]*dx
		
	return integral

def numpy_midpoint_integrate(f,a,b,N): #interval e: [b, a]

	""" uses midpoint sampling to approximate integral"""

	dx = (b-a)/float(N)
	
	x = np.linspace((a+(dx/2.)),(b+(dx/2.)),N+1) # centeres?
	#print(x[-1])
	#print(x[:-1])
	function = np.asarray(f(x[:-1])) # integral += f(i*dx - (dx/2))*dx
	#print(function)
	integral = np.sum(function)*dx
	if (np.size(function) == 1):
		integral = integral*N # handles constant functions
	#for i in range(1,N+1): # using trailing edge point
	#	integral += function[i]*dx
		
	return integral



def get_numpy_function_samples(f,a,b,N):
	x = np.linspace(a,b,N)
	function = f(x)
	if (np.size(function) == 1):
		function = np.full(N,f(x))
	return function


	


def numba_integrate(f,a,b,N): #interval e: [b, a]
	dx = (b-a)/float(N)
	function = get_numpy_function_samples(f,a+dx,b+dx,N+1) #probably faster to call outside, but that breaks convention
	#numba cant optimize if f is not an array like or scalar
	#print(function)
	
	"""
	x = np.linspace((a+dx),(b+dx),N+1) # uses leading point?
	
	function = np.asarray(f(x[:-1]))
	"""
	@jit(nopython=True)
	def numbiate(f,a,b,N):
	#intermediate function to optimize numba
		
		intr = 0
		for i in range(0,N): # using trailing edge point	
			intr += function[i]*dx 
		return intr
	integral = numbiate(function,a,b,N)
	return integral


def numba_midpoint_integrate(f,a,b,N): #interval e: [b, a]
	dx = (b-a)/float(N)
	function = get_numpy_function_samples(f,a+(dx/2.),b+(dx/2.),N+1) #probably faster to call outside, but that breaks convention
	#numba cant optimize if f is not an array like or scalar
	
	@jit(nopython=True)
	def numbiate(f,a,b,N):
	#intermediate function to optimize numba
			
		intr = 0
		for i in range(0,N): # using trailing edge point	
			intr += function[i]*dx 
		return intr
	integral = numbiate(function,a,b,N)
	return integral


