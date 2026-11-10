'''def sum(): #defining a function
    a=12
    b=24
    print(a+b)
#calling a function 
sum()'''

def sum(a , b): #a and b are called parameter
    c=a+b 
    print(c) 

sum(23,43) # 23 and 43 are called positional arguments 
sum(b=14 , a=10) #these are called keyword argument
 #default arguments : when we pass the value of parameters at the time of funciton creation e.g def sum(a=23 , b=32)
 #WHAT IS GOLBAL VARIABLE ??

def g(x):
    print(x)
    print(x+1)
y=5
g(y)
print(y) 
print(x)

#-----------------------------------
def f(y):
    y=1
    y+=1
    print(y)
x=5
f(x)
print(x)