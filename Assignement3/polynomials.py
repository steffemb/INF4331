class Polynomial:

    #polynomials are defined p = a_0 + a_1 x + .... + a_n x^n 

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with 
        the i-th element being the coefficient a_i."""
        #raise NotImplemented
        self.coefficients = coefficients

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        
        deg = 0
        for i in range(len(self.coefficients)):
            if (self.coefficients[i] != 0):
                #print("deg i = %i" %i)
                deg = i
        return deg 
        
        #raise NotImplemented

    def coefficients(self):
        """Return the list of coefficients. 

        The i-th element of the list should be a_i, meaning that the last 
        element of the list is the coefficient of the highest degree term."""
        return self.coefficients
        #raise NotImplemented

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        result = 0
        for i in range(len(self.coefficients)):
            intermediate = 1
            for k in range(i):
                intermediate *= x
            result += self.coefficients[i]*intermediate
        return result

        #raise NotImplemented

    
    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""
        w = Polynomial([])

        if (isinstance( p, int )):
            for i in range(len(self.coefficients)):
                w.coefficients.append(self.coefficients[i])
                #w.coefficients = self.coefficients
                w.coefficients[0] = self.coefficients[0] + p
        elif (isinstance( p, Polynomial )):
            if (len(p.coefficients) < len(self.coefficients)):
                #w.coefficients = self.coefficients
                for i in range(len(p.coefficients)):
                    w.coefficients.append(self.coefficients[i] + p.coefficients[i])
                for i in range(len(p.coefficients),len(self.coefficients)):
                    w.coefficients.append(self.coefficients[i])
            else:
                #w.coefficients = p.coefficients
                for i in range(len(self.coefficients)):
                    w.coefficients.append(self.coefficients[i] + p.coefficients[i])
                for i in range(len(self.coefficients),len(p.coefficients)):
                    w.coefficients.append(p.coefficients[i]) #print("self = %i, ext = %i"%(self.coefficients[i], p.coefficients[i]))
                    #w.coefficients.append(self.coefficients[i] + p.coefficients[i])
                    #print(w.coefficients[i])


        else:
            raise ArithmeticError
        #print(w.coefficients)

        return w
        #raise NotImplemented
        
    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int. 

        If p is not an int or Polynomial, should raise ArithmeticError."""

        w = Polynomial([])
        if (isinstance( p, int )):
            w.coefficients = self.coefficients
            w.coefficients[0] = self.coefficients[0] - p
        elif (isinstance( p, Polynomial )):
            if (len(p.coefficients) < len(self.coefficients)):
                #w.coefficients = self.coefficients
                for i in range(len(p.coefficients)):
                    w.coefficients.append(self.coefficients[i] - p.coefficients[i])
                for i in range(len(p.coefficients),len(self.coefficients)):
                    w.coefficients.append(self.coefficients[i])
            else:
                #w.coefficients = p.coefficients
                #print(self.coefficients)
                #print(p.coefficients)
                for i in range(len(self.coefficients)):
                    w.coefficients.append(self.coefficients[i] - p.coefficients[i])
                for i in range(len(self.coefficients),len(p.coefficients)):
                    w.coefficients.append( -1*(p.coefficients[i]) )
                
        else:
            raise ArithmeticError

        return w

        #raise NotImplemented

    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""
        dummys = self.coefficients
        if (isinstance( c, int )):
            for i in range (len(self.coefficients)):
                dummys[i] = c*self.coefficients[i]
        else:
            raise ArithmeticError
        return Polynomial(dummys)
        #raise NotImplemented


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""

        dummys = self.coefficients
        if (isinstance( c, int )): #what is rmul? no raise errors?
            for i in range (len(self.coefficients)):
                dummys[i] = c*self.coefficients[i]

        return Polynomial(dummys)

        #raise NotImplemented
    
    def __repr__(self):
        """Return a nice string representation of polynomial.
        
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        string = ""
        for i in range (2,len(self.coefficients)-1):
            if (self.coefficients[i] == 0):
                string = string
            elif(self.coefficients[i] < 0):
                string = " - %i"%((-1)*self.coefficients[i]) + "x^%i"%i +string
            else:
                string = " + %i"%self.coefficients[i] + "x^%i"%i +string
        
        if (self.coefficients[1] == 0):
            string = string
        else:
            string = string + " + %i"%self.coefficients[1] + "x"
        if (self.coefficients[0] == 0):
            string = string
        else:
            string = string + " + %i"%self.coefficients[0]
        if (abs(self.coefficients[-1])>1):
            string = "%i"%self.coefficients[-1] + "x^%i"%(len(self.coefficients)-1) +string #no handling if a_0 = 0
        elif (self.coefficients[-1] == 1):
            string = "x^%i"%(len(self.coefficients)-1) +string
        elif (self.coefficients[-1] == -1):
            string = "-x^%i"%(len(self.coefficients)-1) +string
        elif (self.coefficients[-1] == 0):
            string = string[3:]
            
            
            
            
        return string

        #raise NotImplemented

    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""

        if (len(self.coefficients) != len(p.coefficients)):
            return False
        else:
            result = 0
            for i in range(len(self.coefficients)):
                result += self.coefficients[i]-p.coefficients[i]
            if(result == 0):
                return True
            else:
                return False

        #raise NotImplemented

def sample_usage():
    h = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    g = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3
    
    
    print("The value of {} at {} is {}".format(h, 7, h(7)))

    print("The coefficients of {} are {}".format(h, h.coefficients))

    
    print("\nAdding {} and {} yields {}".format(h, g, h+g))

    h, g, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )
    
    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        h, g, r, h+g == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        h, g, r, h-g == r
    ))

sample_usage()
