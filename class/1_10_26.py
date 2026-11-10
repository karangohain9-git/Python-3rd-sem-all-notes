#matplotlib
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use("default")
df = pd.read_csv("class\sharma-kohli.csv")
# print(df.head())
plt.plot(df["index"] , df["RG Sharma"] , label="RG Sharma" , linestyle="--")
plt.plot(df["index"] , df["V Kohli"] , label="V Kohli")
# print(plt.style.available) : it prints all the styles available in matplotlib
# plt.style.use("fivethirtyeight")
# print(plt.show())
# plt.plot(df["index"] , df["V Kohli"])
plt.style.available
plt.style.use("fivethirtyeight")
plt.legend(loc="best") #shows the label
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Career comparison")

print(plt.show())

#label , .legend() and loc works together 
#label : gives name to each line 
# .legend() : shows the labels of the plotted lines on the graph
# loc : loc means location , tells where to place the legend , some loc are - best , upper left , upper right , lower left , lower right , center 
