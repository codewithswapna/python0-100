#1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 
def div(num1, num2):
   
    if num2 != 0:
        return num1 / num2
    else:
        return "Division by zero is not allowed!"

number1 = float(input("Enter the first number (numerator): "))
number2 = float(input("Enter the second number (denominator): "))

result = div(number1, number2)
print(f"The result of dividing {number1} by {number2} is: {result}")


#2.Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number
def square(num):
    return num ** 2

number = float(input("Enter a number: "))

result = square(number)
print(f"The square of {number} is: {result}")


#3.Using max() and min() functions display the maximum and minimum of 5 random numbers. 
import random

numbers = [random.randint(1, 100) for _ in range(5)]

print("The generated numbers are:", numbers)

maximum = max(numbers)
minimum = min(numbers)

print(f"The maximum number is: {maximum}")
print(f"The minimum number is: {minimum}")


#4.Accept a name from the user and display that in lower case using lower() function

name = input("Enter a name: ")

lowercase_name = name.lower()

print(f"The name in lowercase is: {lowercase_name}")
