# import matplotlib.pyplot as plt 
# import pandas as pd 
# df = pd.read_csv("class\sharma-kohli.csv")
# # print(df.head())
# plt.style.use("ggplot")
# plt.plot(df["index"] , df["RG Sharma"] , label="Rg sharma")
# plt.plot(df["index"] , df["V Kohli"] , label="virat ")
# plt.legend(loc = "best")
# plt.xlabel("years")
# plt.ylabel("runs")
# plt.title("career comparison")
# print(plt.show())
# import matplotlib.pyplot as plt 
# sales  = [50000 , 75000 , 30000]
# categories = ["android" , "ios" , "others"] 
# color = ["red" , "green" , "yellow"]
# plt.pie(sales , 
#         labels=categories,
#         autopct="%0.0f%%",
#         explode=[0.1 , 0 , 0],
#         startangle=45,
#         colors=color)
# plt.figure(figsize=(7,8))
# print(plt.show())
import matplotlib.pyplot as plt
sales= [40000 , 60000, 25000 , 15000 , 30000]
categories  = ["laptop" , "mobile" , "tablet" , "headphone" , "smartwatch"]
color =["red" , "green" ,"yellow" , "blue" , "orange" ]
plt.pie(sales ,
        labels=categories,
        autopct = "%0.0f%%" , 
        explode = [0 , 0.1 , 0 , 0 , 0],
        startangle = 45,
        colors=color,)
plt.figure(figsize=(6 , 8))
print(plt.show())