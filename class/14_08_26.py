d={
    "name":"karan",
    "roll":15,
    "age":29,
    "marks":[70,78,80,90,89],
}
# print(d);
#UPDATING VALUE INSIDE THE DICTIONARIE
# d["age"]=22;
# print(d)
# d["marks"][0]=34;
# print(d);
# d["id"]=23; # if we update a key that is not in the dictinary , it goes inside the dictionarie
# print(d);
# #items have two items in it i.e key and value , and they are separated by a comma(,)
# print(d.items());

# for key , values in d.items() :
    
#    print(key)
#    print(key,":",d[key])
#    print(d.get(key))

#deleting items from dictionary
del d["age"];
poped_item=d.pop("name");
d.clear()
print(d);
print(poped_item)