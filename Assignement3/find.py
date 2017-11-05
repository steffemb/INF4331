#!/usr/bin/env python
from math import sin
import sys
import os

#May need Root Permission!! run as "Sudo" (ex. sudo python find.py .gif )

#script for recursive search of directory and subdirectory for files whose name contains the string (arg 1). arg2 is the directory.

print(" ")
print("Searching")
print(" ")

name = sys.argv[1] # no cast, default is string?

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


if (len(sys.argv) > 2): #if not home directory is default
	directory = sys.argv[2]
	rec_search(name,directory)
	
else:
	rec_search(name)


print(" ")
print("End of Search")
print(" ")


"""
steffen@steffen-MS-7792:~/Main/inf4331/Assignement3$ sudo python find.py .py /home/steffen/Main/inf4331/
 
Searching
 
/home/steffen/Main/inf4331//Assignement3/find.py
/home/steffen/Main/inf4331//Assignement3/polynomials.py
 
End of Search
 
"""
