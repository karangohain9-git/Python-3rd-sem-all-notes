#set 
# set is unordered and can't store duplicate values , uses curly brackets 
'''s1 = {1,2,3,4,2,2,2}
print(s)

s2={4,3,1,2}'''
#s1 and s2 are the same set , order of items dosen't matter and indexing dose not matter
# s[0] is not valid 
# s = {1,2,3,4,1,1,1}
# s.add(5)
# print(s)

#update : used to add multiple items 
'''
s={1,2,3}
s.update([4,5,6])
print(s)'''

#s={1,2,4,4,5,6}
'''s.discard(5)
print(s)
s.pop() # randomly deletes item
print(s)
s.remove(2)
print(s)'''
'''del s #deletes the entire set 

print(s)'''

#clear : deletes the elements inside the set , but the set still exists 
#union : joins two set , prints only the unique items
'''s1 = {"A","B","C",23,True}
s2 = {"B", "C", "D"}'''
'''new_set=s1.union(s2)
print(new_set)'''
#intersection : prints the common items 
''''print(s1.intersection(s2))  
print(s1&s2) #alternate method to find intersection
print(s1|s2)'''
#how to prove set has no indexing.....
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1-s2)
print(s2-s1)

