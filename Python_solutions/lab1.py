'''1- Calculate the multiplication and sum of two numbers'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
multiplication = num1 * num2
summation = num1 + num2

print(f"Multiplication: {multiplication}")
print(f"Sum: {summation}")

'''2-Declare two variables and print that which variable is largest using ternary operators'''
a = 10
b = 20
largest = a if a > b else b

print(f"The largest variable is: {largest}")


'''3-Python program to convert the temperature in degree centigrade to Fahrenheit'''
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


'''4-python program to find the area of a triangle whose sides are given'''
import math

a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The area of the triangle is: {area}")
