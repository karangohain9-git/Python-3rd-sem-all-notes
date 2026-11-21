# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv("class\sharma-kohli.csv")
# plt.style.use("default")
# plt.plot(df["index"] , df["V Kohli"] , label="virat kohli" , linestyle="--")
# plt.plot(df["index"] , df["RG Sharma"] , label="rohit sharma")
# plt.legend(loc="best")
# plt.xlabel("years")
# plt.ylabel("runs")
# plt.title("career runs")
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv(r"class\batter.csv")
# #sampling
# ndf = df.head(100).sample(25 , random_state=42)
# #styling and figure size
# plt.style.use("default")
# plt.figure(figsize=(12 , 10))
# #plotting
# plt.scatter(ndf["avg"] , ndf["strike_rate"] , s=ndf["runs"]*0.5 , color="green")
# plt.axhline(130 , color="red")
# plt.axvline(30 , color="blue")
# #giving names to the bubbles
# for i in range(ndf.shape[0]):
#     plt.text(ndf["avg"].values[i] , ndf["strike_rate"].values[i] , ndf["batter"].values[i])

# plt.xlabel("runs")
# plt.ylabel("rate")
# plt.title("career scores")
# plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd
# df = pd.read_csv(r"class\batter.csv")
# ndf = df.head(605).sample(500 , random_state=30)
# plt.style.use("default")
# plt.figure(figsize=(20 , 15))
# plt.scatter(ndf["avg"] , ndf["strike_rate"] , s = ndf["runs"]*0.5 , color="green")
# plt.axhline(120 , color="blue")
# plt.axvline(25 , color="red")
# for i in range(ndf.shape[0]):
#     plt.text(ndf["avg"].values[i] ,ndf["strike_rate"].values[i] ,
#              ndf["batter"].values[i])

# plt.xlabel("avg")
# plt.ylabel("runs")
# plt.title("career scores")
# plt.show()

# import matplotlib.pyplot as plt
# sales = [5000 , 6000 , 7000 ,3400]
# categories = ["android" , "ios"  , "others","motalauda"]
# color =["red" , "green" , "yellow","blue"]
# plt.figure(figsize=(5,5))
# plt.style.use("fivethirtyeight")
# plt.pie(sales,labels=categories , autopct="%0.0f%%" , explode=[0,0,0,0] , startangle=30 ,colors=color)
# plt.show()
# import matplotlib.pyplot as plt
# categories = ["rent" , "food", "transport" ,"entertaintment" , "savings"]
# expense =[12000 , 5000 , 2000 , 1500 , 4500]
# plt.figure(figsize = (6,6))
# plt.pie(expense , labels=categories , autopct ="%0.0f%%" , startangle=30)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Q1", "Q2", "Q3", "Q4"]
sales_2025 = [40, 55, 60, 75]
sales_2026 = [50, 65, 70, 90]

x = np.arange(len(categories))  # Numeric positions: [0, 1, 2, 3]
width = 0.35  # Width of each individual bar

# Shift first set left by width/2, second set right by width/2
plt.bar(x - width / 2, sales_2025, width, label="2025", color="skyblue")
plt.bar(x + width / 2, sales_2026, width, label="2026", color="orange")

plt.xticks(x, categories)  # Put category names back on the X-axis
plt.ylabel("Sales (in Lakhs)")
plt.title("Quarterly Sales Comparison")
plt.legend()
plt.show()
