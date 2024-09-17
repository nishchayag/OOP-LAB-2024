# WAP TO COMPUTE DISTANCE B/W 2 POINTS IN PYTHON
import math as m
x1 = int(input("Enter first X coord: "))
y1 = int(input("Enter first Y coord: "))
x2 = int(input("Enter second X coord: "))
y2 = int(input("Enter second X coord: "))
dist = m.sqrt(pow((x1-x2) , 2) + pow((y1-y2) , 2))
print(dist)

# WAP TO INPUT LIST FROM USER(25 ELE), CALC MEAN,MEDIAN,MODE
from statistics import mean, median, mode
user_list = []
list_size = int(input("Enter the size of the list being divisible by 5: "))
for i in range(list_size):
    num = float(input(f"Enter number {i+1}: "))
    user_list.append(num)

mean_value = mean(user_list)
median_value = median(user_list)

try:
    mode_value = mode(user_list)
except:
    mode_value = "No unique mode found"

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

newList = []

for i in range (list_size/5):
    for j in range (i*5,((i*5)+5)):
        newList[i][j] = newList[j]

evenList = []
oddList = []

for i in range(list_size/5):
    if(i%2 == 0):
        for j in range(5):
            evenList.append(newList[i][j])
    else:
        for j in range(5):
            oddList.append(newList[i][j])


# WAP TO CALC AREA OF A CIRCLE TAKING PI AS CONSTANT
PI = 3.14
r = float(input("Enter the radius of the circle: "))
area = PI * pow(r,2)
print(f"Area of the circle is {area}")
