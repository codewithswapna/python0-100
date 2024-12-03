#1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

num1 = 10
num2 = 2

result = div(num1, num2)
print(f"The division of {num1} by {num2} is: {result}")


#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 

def square(num):
    return num ** 2

number = 5

result = square(number)
print(f"The square of {number} is: {result}")


#3.Using max() and min() functions display the maximum and minimum of 5 random numbers. 

import random

random_numbers = [random.randint(1, 100) for _ in range(5)]

print("Random numbers:", random_numbers)

max_num = max(random_numbers)
min_num = min(random_numbers)

print("Maximum number:", max_num)
print("Minimum number:", min_num)


#4.Accept a name from the user and display that in lower case using lower() function

name = input("Enter your name: ")

lower_case_name = name.lower()
print("Your name in lowercase is:", lower_case_name)