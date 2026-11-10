# import numpy as np
# arr=np.arange(20)
# reshapeArr=arr.reshape(4,5)#should be multiple of 20 
# #print(arr)
# # print()
# print(reshapeArr)
# #---------------------------
# print()
# #to print particular row in a 2D numpy arr 
#print(reshapeArr[0][1:4])
# print(reshapeArr[3][3:])
# print(reshapeArr[2][::-1])
# print()
# #to print columns 
# #syntax arr[row , columns]
# print() 
# print(reshapeArr[: , 0])
# print()
# print(reshapeArr[1:3 , 2:4])
# # print()
# print(reshapeArr[0: , 1:4])

#CREATING A NUMPY ARRAY USING LIST - method 2
#in numpy we can control the size in memory 
#in numpy array the size should be same
# import numpy as np 
# li = [[3,4] , [4,5] , [6,70]]
# print(type(li))
# arr2=np.array(li)
# print(arr2)

#METHOD - 3
# import numpy as np
# np.eye(3)
# np.identity(3) #eye and identity method as same , alternate method

#METHOD - 4
# import numpy as np
# np.zeros((3,5))
# print()
# #method - 5 
# import numpy as np 
# np.ones((3,4))
# print()
# #------------
# import numpy as np #used to create graphs 
# np.linspace(0,10,2)
#  IMP : WHAT IS THE DIFFERENCE BETWEEN arange() and linspace() ?
#in arange() we specify steps/gap
#in linspace() we specify the number of values 

#how to calculate linspace
#spacing = stop-start/number of values - 1
#eg linspace(0 , 10 , 5)
#spacing = 10 - 0 / 5 - 1