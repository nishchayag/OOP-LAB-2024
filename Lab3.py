# WAP A PROGRAM TO TAKE INPUT OF NAME REG. NUMBER AND FATHER'S NAME OF THE USER ALL IN 1 VARIABLE AND SLICE THE REG NO. OUT OF THE FIRST STRING AND STORE IT IN ANOTHER VARIABLE USING LOOPS

x = input("Enter your name: ") + " "
len1 = len(x)
x = input("Enter your Registration Number: ") + " "
len2 = len(x)
x = input("Enter your Father's name: ")
y = ''
for i in range(len1,len2-1):
    y += x[i]

print(y)


# WAP TO FIND IF A NUMBER IS PRIME OR NOT

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#WAP TO CHECK IF A GIVEN NUMBER IS PALINDROME OR NOT
def is_palindrome(number):
    return str(number) == str(number)[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# WAP TO FIND THE GRADE OF A STUDENT USING A GIVEN PERCENTAGE
def find_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'

percentage = float(input("Enter the student's percentage: "))

if 0 <= percentage <= 100:
    grade = find_grade(percentage)
    print(f"The student's grade is: {grade}")
else:
    print("Invalid percentage! Please enter a value between 0 and 100.")

# WAP TO BUILD A SIMPLE CONSOLE BASED CALCULATOR 
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

print("Simple Calculator")

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter the second number: "))

result = calculate(num1, num2, operator)

print(f"Result: {result}")
