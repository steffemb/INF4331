from integrator import *
from numpy_integrator import *
from numba_integrator import *
from cython_integrator import *



"""
Then, write a new script which uses all of the methods you now have written
to compute the integral of f (x) = sin(x) from x = 0 to x = PI. The real answer
is 2. For each of your functions, find the required N such that you get to within
10 −10 of the actual answer.
Name of files: integrator comparison.py, report4.txt
"""

def plot_errors_new(minimum = 2,maximum=75, method1 = "integrate", method2 = "midpoint_integrate", figname = "quadratic_error.png"):
	#plots difference of error of two scheemes over a range of N's
	n = maximum-minimum #number of integrals, not same as in integral()
	integrals1 = []
	integrals2 = [] # bonus
	exact = []
	N_list = []
	method1 = globals()[method1]
	method2 = globals()[method2]
	for i in range(minimum,maximum):
		N=i #N = int((float(maximum-minimum)/n)*i)
		
		if (N<1): N=1
		f = lambda x: x*x #test function
		integrals1.append(abs(method1(f,0,1,N)-float(1/3)))
		integrals2.append(abs(method2(f,0,1,N)-float(1/3)))
		N_list.append(N)
		#exact.append(float(1/3))
	plt.plot(N_list,integrals1, label = "edgepoint scheme")
	#plt.hold('on')
	plt.plot(N_list,integrals2, label = "midpoint scheme")
	#plt.plot(N_list,exact, label = "exact")
	plt.legend()
	plt.xlabel("N (number of sampling points)")
	plt.ylabel("error (computed abs(integral(N)-exact)")
	plt.savefig(figname)
	#plt.show()

def find_N_of_2schemes(minim=2, maxim = 200000, step = 100, method1 = "integrate", method2 = "midpoint_integrate"):
	print("finding N for method 1 = %s and method 2 = %s" %(method1, method2))	
	method1 = globals()[method1]
	method2 = globals()[method2]
	exact = 2.
	ebs = 10**(-10)
	
	for N in range(minim,maxim,1000):
		#x = np.linspace(0,np.pi,N)
		error1 = abs(method1(np.sin,0,np.pi,N)-exact)
		#print(N)
		if(error1<ebs):
			for k in range(N-1000,N+1000):
				#result1 = method1(np.sin,0,1,N)
				error1 = abs(method1(np.sin,0,np.pi,N)-exact)
				#print(error1)
				if(error1<ebs):
					#print("N for method 1 is %i" %(k))
					for q in range(k-100,k+100):
						#result1 = method1(np.sin,0,1,N)
						error1 = abs(method1(np.sin,0,np.pi,N)-exact)
						#print(error1)
						if(error1<ebs):
							#print("N for method 1 is %i" %(k))
					
							N1 = q
							break
					
					
					break
					
			break
		
	print("N for method 1 is %i" %(N1))
	N = 0
	for N in range(minim,maxim,1000):
		#print(N)
		#x = np.linspace(0,np.pi,N)
		error2 = abs(method2(np.sin,0,np.pi,N)-exact)
		if(error2<ebs):
			for k in range(N-1000,N+1000):
				error2 = abs(method2(np.sin,0,np.pi,N)-exact)
				#print (k)
				if(error2<ebs):
					for q in range(k-100,k+100):
						error2 = abs(method2(np.sin,0,np.pi,N)-exact)
						#print (k)
						if(error2<ebs):
							#print("N for method 2 is %i" %(k))
							N2 = q
							break
					
					break
			break
		


	#print("not found, increase maximum")
	print("N for method 2 is %i" %(N2))
	return 0
	

if __name__ == "__main__":
	#f = lambda x: x*x #test function
	#print((numpy_integrate(f,0,1,100)))
	
	plot_errors_new(method1 = "numba_integrate", method2 = "numba_midpoint_integrate", figname = "quadratic_error_numba.png")
	check_schemes()
	
	"""
	find_N_of_2schemes(minim=2, maxim = 20000000, step = 100, method1 = "integrate", method2 = "midpoint_integrate")     
	find_N_of_2schemes(minim=2, maxim = 20000000, step = 100, method1 = "numpy_integrate", method2 = "numpy_midpoint_integrate")     
	find_N_of_2schemes(minim=2, maxim = 20000000, step = 100, method1 = "numba_integrate", method2 = "numba_midpoint_integrate")     
	find_N_of_2schemes(minim=2, maxim = 20000000, step = 100, method1 = "cython_integrate", method2 = "cython_midpoint_integrate")     
	
	"""
	"""
	printout:
	finding N for method 1 = integrate and method 2 = midpoint_integrate
	N for method 1 is 127902
	N for method 2 is 89902
	finding N for method 1 = numpy_integrate and method 2 = numpy_midpoint_integrate
	N for method 1 is 127902
	N for method 2 is 89902
	finding N for method 1 = numba_integrate and method 2 = numba_midpoint_integrate
	N for method 1 is 127902
	N for method 2 is 89902
	finding N for method 1 = cython_integrate and method 2 = cython_midpoint_integrate
	N for method 1 is 127902
	N for method 2 is 89902
	"""
