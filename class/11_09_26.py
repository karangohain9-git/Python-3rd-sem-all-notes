#IMPORTANT FOR PRACTICAL and sessional gonna have a lot of questions from this part 
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
print(df.tail(3))
print(df.groupby("sex").count())#gives data of the every row 
print(df.groupby("sex").size())
#imp question : difference between size and count 
#size(): counts all values including NaN 
#count() : counts all non NaN values 
#Q1)what is the average age of male and female boarding in titanic
# print()
# #sol-1:
# # print(df.groupby("sex")["age"].mean())#gives the average age of male and female
# # print()
# # print(df.groupby("sex")["age"].max())
# print()
# print(df.groupby("sex")["age"].agg(["min","max", "mean" , "std" , "var"]))
# #to find more than one 
# print()
# print(df.groupby("sex")[["age","fare"]].agg(["min","max", "mean" , "std" , "var"]))

# # {"age":"min",
# #  "fare":"max"}#if in questions asks to find the min of age but max in fare, we need to make a dictionary like this
# print(df.groupby("sex")[["age","fare"]].agg({"age":"min",
#  "fare":"max"})) #it gives us the min of age and max of fare
# #groupby is done in categorical columns 

# print()
#q) har class me kitne male h aur kitne female h ?
# print(df.groupby(["pclass","sex"]).size())
#q)find out the maximum fare payed by each gender in each calsses 
print()
# print(df.groupby(["sex","pclass"])["fare"].max())
# print()
# print(df.groupby(["sex","pclass"]).agg({"fare":"max"}))#alternate method

#Q)find the percentage and number of survival for each gender



print(df.groupby(["sex" , "survived"]).size())
print()
print(df.groupby(["sex" , "survived","pclass"]).size())
#in table 0-not survived , 1-survived
#practice conditional based questions (generate questions from ai)
#Q)what is the percentage of male and female who actually smokes using tips i.e sns.load_dataset("tips")