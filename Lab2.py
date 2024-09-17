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

# WAP TO READ AND PRINT VALUES OF VARIABLES OF DIFFERENT DATA TYPES WITH THEIR DATAYPE
def print_value_and_type(value, value_type):
    print(f"Value: {value}, Data Type: {value_type}")

int_value = int(input("Enter an integer value:"))
print_value_and_type(int_value, type(int_value).__name__)

float_value = float(input("Enter a float value:"))
print_value_and_type(float_value, type(float_value).__name__)

string_value = input("Enter a string value:")
print_value_and_type(string_value, type(string_value).__name__)

bool_value = input("Enter a boolean value (True/False):").strip().capitalize()
if bool_value == "True":
    bool_value = True
elif bool_value == "False":
    bool_value = False
else:
    print("Invalid boolean input. Defaulting to False.")
    bool_value = False
print_value_and_type(bool_value, type(bool_value).__name__)


# WAP TO PERFORM ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION ON 2 DECIMAL NUMBERS AND RETURN THE VALUES UPTO 2 DECIMAL PLACES
def perform_calculations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Error! Division by zero."

    print(f"Addition: {addition:.2f}")
    print(f"Subtraction: {subtraction:.2f}")
    print(f"Multiplication: {multiplication:.2f}")
    if isinstance(division, str):
        print(division)
    else:
        print(f"Division: {division:.2f}")

num1 = float(input("Enter the first float number: "))
num2 = float(input("Enter the second float number: "))

perform_calculations(num1, num2)


# WAP TO FIND THE AVERAGE OF TWO NUMBERS AND PRINT THEIR DEVIAITON
def avg_and_deviation(num1,num2):
    avg = (num1+num2)/2
    dev1 = num1 - avg
    dev2 = num2 - avg
    return avg, dev1, dev2

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
average , firstDeviation, secondDeviation = avg_and_deviation(a,b)
print(f"Average is: {average:.2f} \n First deviation is: {firstDeviation} \n Second deviation is: {secondDeviation} \n")


# WAP TO PREPARE A GROCERY BILL. FOR THAT ENTER THE NAME OF THE ITEMS PURCHASED, QUANTITY IN WHICH IT WAS PURCHASED, AND ITS PRICE PER UNIT, THEN DISPLAY THE BILL WITH THE TOTAL AMOUNT TO BE PAID
def prepare_grocery_bill():
    print("Welcome to the Grocery Bill Generator")
    items = []
    while True:
        item_name = input("Enter the name of the item: ")
        quantity = float(input(f"Enter the quantity of {item_name}: "))
        price_per_unit = float(input(f"Enter the price per unit of {item_name}: "))
        total_cost = quantity * price_per_unit

        items.append((item_name, quantity, price_per_unit, total_cost))
        
        more_items = input("Do you want to add another item? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break
    
    total_amount = sum(item[3] for item in items)
    
    print("\n--- Grocery Bill ---")
    print(f"{'Item Name':<20} {'Quantity':<10} {'Price/Unit':<12} {'Total Cost':<10}")
    print("-" * 52)
    
    for item in items:
        print(f"{item[0]:<20} {item[1]:<10.2f} {item[2]:<12.2f} {item[3]:<10.2f}")
    
    print("-" * 52)
    print(f"{'Total Amount':<42} {total_amount:.2f}")

prepare_grocery_bill()
