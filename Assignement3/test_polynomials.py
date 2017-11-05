from polynomials import Polynomial

#unit tests for class Polynomials
#polynomials are defined p = a_0 + a_1 x + .... + a_n x^n 

#p = Polynomial ( [ 5 , 3 , 2 ] )
#q = Polynomial ( [ 4 , 3 ] )
#test = Polynomial ( [ 3 , 0 , 1 , 0 ] )

def test_3_point():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	assert p(0) == 5
	assert p(2) == (2*(2*2) + 3*2 + 5)
	assert p(3) == (2*(3*3) + 3*3 + 5)	


def test_subtract_poly():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	q = Polynomial ( [ 4 , 3 ] )
	#print((p - q).coefficients)
	assert (p - q) == Polynomial ( [ 1 , 0 , 2 ] )
	#p = Polynomial ( [ 5 , 3 , 2 ] ) #weirdness happens when p, q are not redefined after each assert/function operation... ??
	#q = Polynomial ( [ 4 , 3 ] )		
	assert ((q - p)) == Polynomial ( [ -1 , 0 , -2 ] )
	#p = Polynomial ( [ 5 , 3 , 2 ] )
	assert (p - 3) == Polynomial ( [ 2 , 3 , 2 ] )
	
def test_add_poly():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	q = Polynomial ( [ 4 , 3 ] )
	assert (p + q) == Polynomial ( [ 9 , 6 , 2 ] )
	#print((q + p).coefficients)
	assert (q + p) == Polynomial ( [ 9 , 6 , 2 ] )
	#p = Polynomial ( [ 5 , 3 , 2 ] )
	assert (p + 3) == Polynomial ( [ 8 , 3 , 2 ] )

def test_poly_degree():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	q = Polynomial ( [ 4 , 3 ] )
	test = Polynomial ( [ 3 , 0 , 1 , 0 ] ) # several zeros might give issues?
	assert p.degree() == 2
	assert q.degree() == 1
	assert test.degree() == 2
	
def test_mul_poly():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	c = 3
	assert (p * c) == Polynomial ( [ 15 , 9 , 6 ] )
	p = Polynomial ( [ 5 , 3 , 2 ] )
	c = -2
	assert (p * c) == Polynomial ( [ -10 , -6 , -4 ] )

def test_string_poly():
	p = Polynomial ( [ 5 , 3 , 2 ] )
	assert str(p) == "2x^2 + 3x + 5"
	p = Polynomial ( [6 , 0 , -5 , 3 , 2 , 7 , -2 , 0 , 1] )
	assert str(p) == "x^8 - 2x^6 + 7x^5 + 2x^4 + 3x^3 - 5x^2 + 6"
	p = Polynomial ( [0 , 4, -1] )
	assert str(p) == "-x^2 + 4x" # a_n = -1 can be issue?
	p = Polynomial ( [1 , 4, 0] ) #handeling a_n = 0
	assert str(p) == "4x + 1"

test_3_point()
test_subtract_poly()
test_add_poly()
test_poly_degree()
test_mul_poly()
test_string_poly()

print("no errors encountered")

