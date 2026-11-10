'''list = [1 ,2 ,3 ,4, 5]
'''
#len/min/max/sorted
#L = [2,1,5,7,0,2,5,32,2]
'''print(len(L))
print(min(L))
print(max(L))
print(sorted(L,reverse=True))
x=L.count(2) #Count is a methode as it uses dot(.) , and its checks how many times a number is repeating 
print(x)'''


#count , index
'''y=L.index(7)
print(y)
x=L.index(5,3)'''# here 3 is used to check the index of the next 5 after checking the first 5 in the position 2 , checking starts from the next index 3 .By default is gives u the position of the first number z

'''print(x)
print(L.index(-3))'''
#if we use count methode for a number that is not present in the list , the result will be 0

'''l=[34,44,5,564]
print("Memory address of original list :",id(l))
print(sorted(l))
print("memory address of sorted/copy list :",id(sorted(l)))'''
#2D list 
#l=[11,[1,2,4],29,34,[100,1,1010]]
'''print(l[1])
print(l[1][2])'''
#print(l[4][0])
'''p=[1,2,[40,50,[100,1010,1001]],8,9]
print(p[2][2][1])'''

l=[1,2,3,[4,5,6,[7,8,9]],10]
print(l[3][3][0])