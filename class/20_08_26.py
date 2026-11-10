#numpy 
#numpy arrays are fixed in size 
#elements are of same data type 
#module , library , framework ??....
#creating a numpy array 
#pip install numpy
import numpy
a=numpy.arange(5)
print(a.shape)
print(a.ndim )
print(a[-1])
print(a.dtype)
b=a.astype("int8")#astype returns a copy of the original array in int 8 bits and dosen't change the actual array
print(b)
print(b.dtype)
#why numPY is faster ??... bytes 

# import numpy as np 
# a=np.arange(5)
# #what is implicit typecasting ??....
