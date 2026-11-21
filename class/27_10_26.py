#pie chart
import matplotlib.pyplot as plt
sales=[50000,75000,30000]
categories=["Android","Ios","Others"]
color=["red","green","yellow"]
plt.figure(figsize=(6,6))
plt.pie(sales,
        labels=categories,
        autopct="%0.0f%%",
        explode=[0.1,0,0],
        startangle=30,
        colors=color,)

plt.show()

#bar chart
import matplotlib.pyplot as plt

# 1. Define data
subjects = ["Math", "Physics", "Chemistry", "English", "CS"]
marks = [88, 76, 82, 91, 95]

# 2. Set figure size before plotting
plt.figure(figsize=(8, 5))

# 3. Create the bar chart
plt.bar(subjects, marks, color="royalblue", width=0.5)

# 4. Add labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks Scored")
plt.title("Student Exam Performance")

# 5. Display the chart
plt.show()
