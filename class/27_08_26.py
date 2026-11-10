#NUMPY ARRAY OPERATIONS 
# import numpy as np  
# a = np.arange(4).reshape(2,2)
# b = np.arange(4).reshape(2,2)
# # print(a,b)
# # print("Addition:" , a+b)
# print("multiplication:" ,a*b)#it does element * element multiplication 
# print(np.dot(a,b)) #it print the cross multiplication of the matrices .

#RELATIONAL OPERATORS 
# import numpy as np
# a = np.arange(4).reshape(2,2)
# print(a)
# print(a[a>=3])# Boolean masking (it prints the value that satisfies the condition)
# print()
# print(a>=3)#checks and gives the answer in true and false 

#sum of all the elements in an array 
# print(np.sum(a, axis=0)) #axis=0 means column wise sum
# print(np.sum(a, axis=1)) #axins =1 means row wise sum 
# #numpy methods
# np.std(a)
# np.var(a)
# np.prod(a)
# print(np.log(a)) #R1C0
# np.sin(a)
# np.cos(a)


#IMP FOR PRACTICALS
# b=np.array([0,30,45,60,90])
# print(b)
# b=np.deg2rad(b)
# print(np.sin(b))

# import numpy as np 
# x=np.linspace(0,360,100)#in lab exam we will be give this kind of equations and we need to make graph using the equation 
# # y=3*x+1
# # print(y)
# x=np.deg2rad(x)
# y=np.sin(x)
# print(y)
# import matplotlib.pyplot as plt
# plt.plot(y)

#making Sin(x) graph 
import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(0 , 360 , 100)#higher range gives smoother graphs
y= np.deg2rad(x)
z= np.sin(y)
plt.plot(x,z)
plt.show

#PRACTICAL 1 : FIND ALL THE TRIGONOMETRIC VALUES OF MOST COMMONLY USED ANGLES 
# import numpy as np 
# x=np.array([0,30,45,60,90])
# x=np.deg2rad(x)
# y=np.sin(x)
# print(y)


#rv of sum 
# import numpy as np
# a=np.arange(10).reshape(5,2)
# print(a)
# # print(np.sum(a,axis=1))
# # # print(np.sum(a,axis=0))
# # #boolean index
# # print(a>5)
# # print(a[a>5])#a>5 is a boolean index

# #using loop in 2D array
# b=np.arange(10).reshape(5,2)
# # for i in np.nditer(a): #this method unpacks a 2D into a 1D array and then prints it (IMP)
# #     print(i)
# # PRINTING TWO 2D ARRAY
# print(a,b)
# for i,j in np.nditer([a,b]):
#     print(i,j)

#PRACTICAL 2 : iterate through both array together and add the  respective items and return the result in array
# import numpy as np
# a=np.arange(10).reshape(5,2)
# b=np.arange(10).reshape(5,2)

# for i,j in np.nditer([a,b]):
#     c=i+j

import numpy as np
# print(np.random.randint(1,62,3))
# print(np.random.random(10))#any random no from 0 t0 1(0<= number <1)
# print(np.random.random(10)*100) #0<= number <1*100
a=np.arange(10).reshape(5,2)
# print(a)
# print()
# print(np.transpose(a))#finds the transpose of a matrix
# print(a.T)#alternate method to print the transpose

#difference between ravel and flatten
# print()
# # print(a.ravel())
# b=a.ravel() #returns view i.e both arrays are same 
# print(b)
# b[0] = 100
# print(b)
# print()
# print(a)
#flatten gives u the changed array 
c=a.flatten() #returns a cooy
c[0]=1000
print(a)
print()
print()
print(c)

# Main difference
# ravel()	                flatten()
# Usually returns a view	Always returns a copy
# Changes to the result may affect original array	Changes to result do not affect original
# Generally faster	        Generally uses more memory
# Preferred when you don't need an independent copy	   Preferred when you need a separate copy