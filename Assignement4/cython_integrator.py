from integrator import integrate
import numpy
from cython_integrator import cython_integrate
import time


if __name__ == "__main__":
	report = open('report5.txt', 'w')
	f = lambda x: x*x
	a=0
	b=1
	N = 10000

	start1 = time.time()


	integral = cython_integrate(f,a,b,N)
	#print(integral)

	end1 = time.time()
	report.write("time taken for N = %i using cython is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using cython is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using cython slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using cython speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))

	###########################################################

	report.write("------------------------------------------------- \n")

	N = 1000000

	start1 = time.time()


	integral = cython_integrate(f,a,b,N)
	#print(integral)

	end1 = time.time()
	report.write("time taken for N = %i using cython is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using cython is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using cython slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using cython speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))


	report.write("------------------------------------------------- \n")

	N = 10000000

	start1 = time.time()


	integral = cython_integrate(f,a,b,N)
	#print(integral)

	end1 = time.time()
	report.write("time taken for N = %i using cython is %f \n"%(N,end1 - start1))

	start2 = time.time()

	integral = integrate(f,a,b,N)

	end2 = time.time()
	report.write("time taken for N = %i NOT using cython is %f \n"%(N,end2 - start2))


	report.write("the difference of time2-time1 if %f \n"%((end2 - start2)-(end1 - start1)))

	if((end2 - start2) < (end1 - start1)):
		report.write("using cython slowed down the integrator by %i percent \n" %((((end1 - start1)/(end2 - start2))*100)-100))
	if((end2 - start2) > (end1 - start1)):
		report.write("using cython speeds up the integrator by %i percent \n" %(((end2 - start2)/(end1 - start1))*100))
		

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
	report.write("cProfile cython_integrate(): \n")
	pr = cProfile.Profile()
	res = pr.run("cython_integrate(f,a,b,N)")  # res contains the statistics
	#report.write(res.print_stats())
	pr.dump_stats("cython_integrate.prof")  # Dump statistics to file for use with pstats
	

	stats = pstats.Stats("cython_integrate.prof", stream=report)
	stats.sort_stats("time")
	stats.print_stats(5)
	report.close()


