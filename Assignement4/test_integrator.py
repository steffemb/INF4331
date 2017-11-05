from integrator import integrate
from numpy_integrator import numpy_integrate
from cython_integrator import cython_integrate

def test_integral_of_constant_function(N):
	f = lambda x: 2 #Test function
	computed_answer = integrate(f,0,1,N)
	expected_answer = 2
	assert abs(computed_answer-expected_answer) < 1**(-20)

def test_integrals_of_linear_function(N,c=1): #c scales error (order of 1/N)
	f = lambda x: 2*x
	computed_answer = integrate(f,0,1,N)
	expected_answer = float(1)
	error = float(c)/N
	assert abs(computed_answer-expected_answer) < error

def test_numpy_integral_of_constant_function(N):
	f = lambda x: 2 #Test function
	computed_answer = numpy_integrate(f,0,1,N)
	expected_answer = 2
	assert abs(computed_answer-expected_answer) < 1**(-20)

def test_numpy_integrals_of_linear_function(N,c=1): #c scales error (order of 1/N)
	f = lambda x: 2*x
	computed_answer = numpy_integrate(f,0,1,N)
	expected_answer = float(1)
	error = float(c)/N
	assert abs(computed_answer-expected_answer) < error

def test_cython_integral_of_constant_function(N):
	f = lambda x: 2 #Test function
	computed_answer = cython_integrate(f,0,1,N)
	#print(computed_answer)
	expected_answer = 2
	assert abs(computed_answer-expected_answer) < 1**(-20)

def test_cython_integrals_of_linear_function(N,c=1): #c scales error (order of 1/N)
	f = lambda x: 2*x
	computed_answer = cython_integrate(f,0,1,N)
	expected_answer = float(1)
	error = float(c)/N
	assert abs(computed_answer-expected_answer) < error

N = 100
test_integral_of_constant_function(N)
test_integrals_of_linear_function(N,1)
test_numpy_integral_of_constant_function(N)
test_numpy_integrals_of_linear_function(N,1)
test_cython_integral_of_constant_function(N)
test_cython_integrals_of_linear_function(N,1)
print("no errors encountered")
