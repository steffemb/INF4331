# collection of usefull python functions

def write_list_to_file(list_name, file_name):
    f = open(file_name, 'w')
    for item in list_name:
        f.write(item + "\n")

def readfile(read):
    infile = open('%s.txt' % read, 'r')
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    # how many columns?

    while True:
        line = infile.readline()
        if not line:
            break
        numbers = line.split()
        data1 = float(numbers[0])
        data2 = float(numbers[1])
        data3 = float(numbers[2])
        data4 = float(numbers[3])
    
        column1.append(data1)
        column2.append(data2)
        column3.append(data3)
        column4.append(data4)
    infile.close()

    return [column1, column2, column3, column4]


def rec_search(keyword = name,directory = os.environ['HOME']):
	""" 
	Recursive search starting from directory variable

	keyword: is the keyword to be searched for in every filename

	PS: May need Root Permission!!
	"""
	os.chdir(directory)
	current_list = os.listdir(directory)
	for item in current_list:
		if os.path.isdir(directory + '/%s'%item):
			rec_search(keyword,directory = directory + '/%s'%item)
		if keyword in item:
			print(directory+"/"+item)

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

def remove_duplicates(mylist):
    """
    removes anny duplicate entries in a list
    """
    newlist = []
    for i in mylist:
        if i not in newlist:
            newlist.append(i)
    return newlist


