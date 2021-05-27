import pandas
from sklearn.linear_model import LinearRegression
dataset = pandas.read_csv("marks.csv")
y = dataset["marks"]
x = dataset["hrs"].values.reshape(5,1)
mind = LinearRegression()
mind.fit(x,y)
hours = int(input("Please enter the number of hours studied"))
result = mind.predict([[hours]])
print("Your predicted marks would be: {0}".format(result))