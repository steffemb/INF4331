from package.integrator import integrate
from numba import jit
import time
import timeit
import numpy as np


"""
@jit
def integrate(f,a,b,N): #interval e: [b, a]
	#print("integrating %s"%str(inspect.getsourcelines(f)[0][0]))
	dx = (b-a)/float(N)	
	integral = 0
	for i in range(1,N+1): # using trailing edge point
		integral += f(i*dx)*dx
		
	return integral
"""

@jit
def get_function_samples(f,N):
	function=[]
	for i in range(0,N+1):
		function.append(f(i*dx))

	return function


@jit
def get_numpy_function_samples(f,a,b,N):
	x = np.linspace(a,b,N)
	function=f(x)
#	for i in range(0,N+1):
#		function.append(f(i*dx))
	
	return function


def numba_integrate(f,a,b,N): #interval e: [b, a]
	dx = (b-a)/float(N)
	function = get_numpy_function_samples(f,a+dx,b+dx,N+1) #probably faster to call outside, but that breaks convention
	#numba cant optimize if f is not an array like or scalar
	
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


"""
def make_numba_integrate(f):
	@jit(nopython=True)
	def numbaintegrate(a,b,N): #interval e: [b, a]
		#numba cant optimize if f is not an array like or scalar
		#print("integrating %s"%str(inspect.getsourcelines(f)[0][0]))
		dx = (b-a)/float(N)	
		integral = 0
		for i in range(1,N+1): # using trailing edge point
			integral += f(i)*dx #
		
		return integral
	return numbaintegrate
"""

if __name__ == "__main__":

	
	report = open('report4.txt', 'w')

	report.write("TLDR: \n \n Numba makes the integration faster, but the added time taken to initialize the \n function samples makes it not worth it. \n \n numba is unable to handle functions that get a function passed. In that case \n numba only adds overhead \n \n numba + numpy arrays instead of lists speeds up integration if N is large. \n   \n  \n")
	report.write("------------------------------------------------- \n \n")
	f = lambda x: x*x
	a=0
	b=1
	N = 1000
	dx = (b-a)/float(N)

	
	#sample function
	

	start1 = time.time()
	
	
	
	#numba_integrate = make_numba_integrate(f)
	integral = numba_integrate(f,a,b,N)
	

	end1 = time.time()
	report.write("time taken for N = %i using numba is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numba is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numba slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numba speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))

	###########################################################

	report.write("------------------------------------------------- \n")

	N = 10000000

	#print(timeit.timeit(stmt="numba_integrate", setup="from __main__  import numba_integrate"))
	#print(timeit.timeit(stmt="integrate", setup="from __main__  import integrate"))

	start1 = time.time()

	#f_list = [] #set up list to pass to function
	#for i in range(0,N+1):
	#	f_list.append(f(i*dx))

	#function = get_function_samples(f,N)

	#numba_integrate = make_numba_integrate(f)
	integral = numba_integrate(f,a,b,N)

	end1 = time.time()
	report.write("time taken for N = %i using numba is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numba is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 is %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numba slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numba speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))




	"""
	report.write("------------------------------------------------- \n")
	report.write("cProfile integrate(): \n")
	import cProfile
	pr = cProfile.Profile()
	res = pr.run("integrate(f,a,b,N)")  # res contains the statistics
	#report.write(res.print_stats())
	pr.dump_stats("integrate.prof")  # Dump statistics to file for use with pstats
	
	
	import pstats
	stats = pstats.Stats("integrate.prof", stream=report)
	stats.sort_stats("time")
	stats.print_stats(5)


	report.write("------------------------------------------------- \n")
	report.write("cProfile numba_integrate(): \n")
	pr = cProfile.Profile()
	res = pr.run("numba_integrate(f,a,b,N)")  # res contains the statistics
	#report.write(res.print_stats())
	pr.dump_stats("numba_integrate.prof")  # Dump statistics to file for use with pstats
	

	stats = pstats.Stats("numba_integrate.prof", stream=report)
	stats.sort_stats("time")
	stats.print_stats(5)
	


	report.write("------------------------------------------------- \n")
	report.write("Using numpy arrays: \n")
	report.write(" \n")
	"""
	"""
	f = lambda x: x*x
	a=0
	b=1
	N = 10000
	dx = (b-a)/float(N)

	
	#sample function
	

	start1 = time.time()
	
	#function = get_numpy_function_samples(f,a,b,N)
	
	#numba_integrate = make_numba_integrate(f)
	integral = numba_integrate(f,a,b,N)
	

	end1 = time.time()
	report.write("time taken for N = %i using numba is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numba is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numba slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numba speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))

	###########################################################

	report.write("------------------------------------------------- \n")

	N = 10000000

	#print(timeit.timeit(stmt="numba_integrate", setup="from __main__  import numba_integrate"))
	#print(timeit.timeit(stmt="integrate", setup="from __main__  import integrate"))

	start1 = time.time()

	#f_list = [] #set up list to pass to function
	#for i in range(0,N+1):
	#	f_list.append(f(i*dx))

	#function = get_numpy_function_samples(f,a,b,N)

	#numba_integrate = make_numba_integrate(f)
	integral = numba_integrate(f,a,b,N)

	end1 = time.time()
	report.write("time taken for N = %i using numba is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numba is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 is %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numba slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numba speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))




	"""




	report.close()


