import numpy as np
#import inspect
import matplotlib.pyplot as plt

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


def check_schemes(N=3):
#not a part of the assignement:
#check the difference of a trailing point sampling (as in assignement)
# and a midpoint point scheme
	f = lambda x: x*x
	a = 0
	b = 1
	exact = 1/float(3)
	integral1 = integrate(f,a,b,N)
	integral2 = midpoint_integrate(f,a,b,N)

	print("error of integral trailing sampling = %f" %abs(integral1-exact))
	print("error of integral midpoint sampling = %f" %abs(integral2-exact))
	#can check sin function too?

def plot_errors(minimum = 2,maximum=75):
	#plots difference of error of two scheemes ofer a range of N's
	n = 300 #number of integrals, not same as in integral()
	integrals1 = []
	integrals2 = [] # bonus
	exact = []
	N_list = []

	for i in range(1,n):
		N = int((float(maximum-minimum)/n)*i)
		if (N<1): N=1
		f = lambda x: x*x #test function
		integrals1.append(abs(integrate(f,0,1,N)-float(1/3)))
		integrals2.append(abs(midpoint_integrate(f,0,1,N)-float(1/3)))
		N_list.append(N)
		#exact.append(float(1/3))
	plt.plot(N_list,integrals1, label = "assignement")
	#plt.hold('on')
	plt.plot(N_list,integrals2, label = "midpoint scheme")
	#plt.plot(N_list,exact, label = "exact")
	plt.legend()
	plt.xlabel("N (number of sampling points)")
	plt.ylabel("error (computed abs(integral(N)-exact)")
	plt.savefig("quadratic_error_new.png")
	#plt.show()




if __name__ == "__main__":
	#f = lambda x: x*x #test function
	#print((numpy_integrate(f,0,1,100)))
	
	plot_errors()
	check_schemes()

