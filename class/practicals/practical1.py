#find all the trigomonetric values of most commonly used angles
#1 : sin
# import numpy as np
# x = np.array([0,30,45,60,90])
# y = np.deg2rad(x)
# z = np.sin(y)
# print(z)

#imp : 
#to print only one value 
#print(np.sin(np.deg2rad(30)))
#2 : cos
# import numpy as np
# x=np.array([0,30,45,60,90])
# y=np.deg2rad(x)
# z=np.cos(y)
# print(z)

#3 : tan or (sin/cos)
# import numpy as np
# x=np.array([0,30,45,60,90])
# y=np.deg2rad(x)
# z=np.tan(y)
# print(z)

#4 : cot or (cos/sin) or (1/tan)
# import numpy as np
# x=np.array([0,30,45,60,90])
# y=np.deg2rad(x)
# z=1/np.tan(y)
# print(z)

#5 : sec 
# import numpy as np
# x=np.array([0,30,45,60,90])
# y=np.deg2rad(x)
# z=1/np.cos(y)
# print(z)

#6 cosec
import numpy as np
x=np.array([0,30,45,60,90])
y=np.deg2rad(x)
z=1/np.sin(y)
print(z)