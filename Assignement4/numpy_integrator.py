from integrator import integrate
import numpy as np
import time

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



if __name__ == "__main__":
	report = open('report3.txt', 'w')
	f = lambda x: x*x
	a=0
	b=1
	N = 10000

	start1 = time.time()


	integral = numpy_integrate(f,a,b,N)

	end1 = time.time()
	report.write("time taken for N = %i using numpy is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numpy is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numpy arrays slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numpy arrays speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))

	###########################################################

	report.write("------------------------------------------------- \n")

	N = 1000000

	start1 = time.time()


	integral = numpy_integrate(f,a,b,N)

	end1 = time.time()
	report.write("time taken for N = %i using numpy is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using numpy is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using numpy arrays slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using numpy arrays speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))
	
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
	report.write("cProfile numpy_integrate(): \n")
	pr = cProfile.Profile()
	res = pr.run("numpy_integrate(f,a,b,N)")  # res contains the statistics
	#report.write(res.print_stats())
	pr.dump_stats("numpy_integrate.prof")  # Dump statistics to file for use with pstats
	

	stats = pstats.Stats("numpy_integrate.prof", stream=report)
	stats.sort_stats("time")
	stats.print_stats(5)
	report.close()


