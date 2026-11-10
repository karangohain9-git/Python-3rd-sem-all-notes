#file handling 

# TO CREATE A FILE 
f=open("demo.txt","w")
f.write("hello world")
f.close()
#write rewrites the existing text 
#with() #context manager

#TO EDIT AN EXISTING FILE
with open("demo.txt","a") as f: #when we write using with() we dont need to close it again with .close()
    f.write("\nhi assam")