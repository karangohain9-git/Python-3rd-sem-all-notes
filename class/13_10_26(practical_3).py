#imp for lab exam 
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r"class\batter.csv")
ndf = df.head(100).sample(25, random_state=21)
print(ndf.head())
plt.style.use("fivethirtyeight")
plt.figure(figsize=(12 , 10)) #changes the length and breadth of the chart 
plt.scatter(ndf["avg"] , ndf["strike_rate"] , s=ndf["runs"]*0.5 , color="#42f5ec")
plt.axhline(130 , color="red")
plt.axvline(32 , color="green")
for i in range(ndf.shape[0]):
    plt.text(ndf["avg"].values[i] , ndf["strike_rate"].values[i] , ndf["batter"].values[i] )
plt.savefig("batsman.png")
# plt.text(1,1,"point 1") #gives  name to a point at a particular posn

plt.xlabel("x axis")
plt.ylabel("y axis")
print(plt.show())
#difference b/w scatter and bubble chart/plot ?
#use of scatter plot :

#what is corelated graph  ?
#positive and negative corelation ? 
#what is weakly corelated ?
#corelation is given by 3 constants : 1 , 0 , -1
