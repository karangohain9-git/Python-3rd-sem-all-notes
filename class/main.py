'''print("hello world !")
print("karandeep gohain")
print(5+5)
print(10-3)
print(10*3)
print(3**3)
print(100/2)
print(100/3)
print(100//3)
'''
'''''fname="karandeep"
lname="gohain"
print("First name : ",fname)
print("Last name :", lname)'''
'''name=input("what is your name?")
roll=input("what is your roll number?")
address=input("what is your address?")
print("--------------------------")
print("My name is :",name)
print("My roll number is :",roll)
print("MY address is :",address)'''
'''n1=int(input("Enter first number ="))
n2=int(input("Enter second number ="))
n3= n1 + n2
print("The sum of the first and the second number is : ", n3)'''
'''n1=float(input("Enter first number :"))
n2=float(input("Enter second number :"))
print("The sum of the numbers is :",n1+n2)'''

#round(number , digits) function

'''round_func=round(100/3 , 2)
print(round_func)'''

'''name,city = map(str , input("enter name and city :").split())
print("Name : ",name, "\nCity : ",city)'''

'''roll,age = map(int , input("enter roll number and age :").split())
print("Roll number : ", roll , "\nAge : ",age)'''
'''name=input("enter name")
roll = int(input("enter roll number :"))
print(f"My name is :{name} \nRoll number : {roll}")'''
'''x=int(input("enter first number  :"))
y=int(input("enter second number :"))
temp=x
x=y
y=temp
print("Value of x after swapping is :",x)
print("Vaule of y after swapping is :",y)'''

'''print(bool(0))
print(bool(""))
print(bool([]))'''
'''n=False
a=int(n)
print(a)'''
'''a=25
a=float(a)
print(a)
print(type(a))'''

'''b=23.45
b=int(b)
print(b)
print(type(b))'''
'''string="34"
string_convert=int(string)
print(string_convert)
print(type(string_convert))'''
'''year=int(input("enter a year:"))
if(year % 4==0 and year % 100 !=0 or year % 4 ==0):
    print(f"{year} is a leap year")
else :
    print(f"{year} is not a leay year")'''

#arr=[1,2,3,4,5]
'''arr.append(6)
print(arr)'''
'''arr.pop()
print(arr)'''
'''arr.extend([9,10,11])
print(arr)'''
'''arr.remove(1)
print(arr)'''
'''x=arr.pop()
print(x)'''
'''del arr[2]
print(arr)
#pop requires index , and removes requires the element'''

'''li=[1,2,3,4,5]
for item in li : #item can be any name 
    print(item)'''
li=[1,2,3,4,5]
for i in range (len(li)): #range () is a function 
   ''' li.append(li[i]+1)'''
print(li)
