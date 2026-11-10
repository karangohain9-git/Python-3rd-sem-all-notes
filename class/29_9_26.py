#merge types : left , right , inner , outer , full 
#left joint : to join the first table
#Syntax :pd.merge(df1 , df2 , how="left" , on="departmentID")
# import pandas as pd
# employees = pd.DataFrame({
#     "emp_id":[101 , 102 , 103 , 104],
#     "name":["Amit" , "Rahul " , "Priya" , "Neha"],
#     "dept_id":[1 , 2 , 1 , 3]
# })

# departments = pd.DataFrame({
#     "dept_id": [1,2,3],
#     "department":["IT" , "HR" , "Finance"]
# })

# print(pd.merge(employees , departments , how="left" , on="dept_id"))
# print()
# print(pd.merge(employees , departments , how="right" , on="dept_id"))
# print()
# print(pd.merge(employees , departments , how="inner" , on="dept_id"))
# print()
# print(pd.merge(employees , departments , how="outer" , on="dept_id"))
# print()
# print(pd.merge(employees , departments , how="full" , on="dept_id"))

import pandas as pd

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "customer_name": ["Amit", "Rahul", "Priya", "Neha"],
    "city": ["Delhi", "Mumbai", "Pune", "Kolkata"]
})

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004],
    "customer_id": [102, 103, 105, 102],
    "product": ["Laptop", "Mobile", "Tablet", "Mouse"],
    "amount": [60000, 25000, 15000, 1000]
})
#inner joint is used to find the common from both the tables 
# print(pd.merge(left=customers , right=orders , how="inner" , on="customer_id" , indicator=True))

#indicator=True : is a Pandas merge() feature that tells you where each row came from.

# #joint relation are of one-to-many relation
# print()
# print(pd.merge(left=customers , right=orders , how="left" , on="customer_id",indicator=True))
# print()
# print(pd.merge(left=customers , right=orders , how="right" , on="customer_id"))
# print()
# print(pd.merge(left=customers , right=orders , how="outer" , on="customer_id"))
#find all the customer who haven't ordered from the result table
result = pd.merge(customers , orders , on="customer_id" , how="outer" , indicator=True)
print(result)
print()
print(result["_merge"]=="left_only")
#find invalid customers
print(result[result["_merge"]=="right_only"])
#use of pd.concat()
#pd.concat() is used to combine/concatenate DataFrames. The biggest difference from pd.merge() is: merge() combines based on matching columns/keys, while concat() simply joins DataFrames together along rows or columns.
#differnce b/w pd.concat() and pd.merge()?

import pandas as pd
left = pd.DataFrame({
    "name":["amit" , "rahul"],
    'marks':[88 , 90]
})

right = pd.DataFrame({
    'name':["priya" , "neha"],
    "marks":[97,78]
})

concatdf = pd.concat([left , right])
print(concatdf)