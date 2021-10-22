import matplotlib.pyplot as plt
import re

# re.sub(r"\s+", "", string) will remove previous or trailing spaces from the inpute string
x = re.sub(r"\s+", "", input("Please enter values of x-axis saperated with comma: ")).split(",")
y = re.sub(r"\s+", "", input("Please enter values of y-axis saperated with comma: ")).split(",")
if len(x) != len(y):
    exit("x and y axis aren't equal cannot produce graph")

# Setting labels
lables = list(input("Please enter title, x-axis, and y-axis lable saperated with comma\nLike: Marks,Score,Subject(Press enter to avoid): ").split(","))
if len(lables) != 3:
    lables = ["Graph", "x-axis", "y-axis"]

# Plotting
ch = input("Type 's' to scatter and 'p' for line plot, ANYOTHER KEY for all functions: ")
if ch == 's':
    plt.scatter(x, y, alpha=0.5)
elif ch == 'p':
    plt.plot(x, y, alpha=0.5)
else:
    plt.plot(x, y, alpha=0.5)
    plt.scatter(x, y, alpha=0.5) 

plt.title(lables[0])
plt.xlabel(lables[1])
plt.ylabel(lables[2])
plt.style.use('seaborn')
plt.show()