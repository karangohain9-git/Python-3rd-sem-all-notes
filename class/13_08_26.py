#dictionary
#they are mutable
student={
    "name":"karan",
    "roll":24,
    "age":19,
    "marks":[40,50,44,34,79],
}
'''print(student["name"]);#to access the name
print(student["age"]);'''
print(student["marks"]);
print(student["marks"][3]);#to print a specific item from a list 
print(student["marks"][::2]);#slicing in dictionaries 
print(student["marks"][::4]);
