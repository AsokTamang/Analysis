import numpy as np
import time

#numpy arrays occupy less memory as well as they are much faster compared to the python lists
#as well as numpy has a lot of built-in functions

l1=np.arange(10)  #this np.arange creates the list upto 9
print(l1)
l2=np.arange(10)
start_time = time.time()
l3 = l1 + l2   #vector addition of arrays
endtime = time.time()
print(endtime-start_time)

rev=np.array([40,30,70])
rev2=np.array([[40,30,70],[90,100,200]])
print(rev.ndim)
print(rev2.ndim)  #here .ndim gives us the number of dimension of an array
print(rev2[1,1])  #based on indexing, we are getting the number
