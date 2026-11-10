import matplotlib.pyplot as plt
sales=[50000,75000,30000]
categories=["Android","Ios","Others"]
color=["red","green","yellow"]
plt.pie(sales,
        labels=categories,
        autopct="%0.0f%%",
        explode=[0.1,0,0],
        startangle=30,
        colors=color,)
plt.figure(figsize=(79,100))
print(plt.show())